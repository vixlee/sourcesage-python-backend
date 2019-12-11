from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_mail import Mail,  Message
from flask_cors import CORS

import os
import datetime
import hashlib
import sys
try:
    import user_api.config_app as config_app
    from user_api.common import AESCipher, create_db_file, validate_password_strength
    from user_api.models import User, db, user_schema, login_form_schema, reset_password_schema
except:
    import config_app as config_app
    from common import AESCipher, create_db_file, validate_password_strength
    from models import User, db, user_schema, login_form_schema, reset_password_schema


app = Flask(__name__)
CORS(app)
app.config.from_object(config_app)
db.init_app(app)
jwt = JWTManager(app)
mail = Mail(app)
cipher = AESCipher(app.config['SECRET_KEY'])

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
if not os.path.isfile(dir_path+'/developement.db'):
    create_db_file(dir_path+'/developement.db')

@app.route("/api/auth/sign-up", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"message": "Data must be a JSON object"}), 400
    errors = user_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400
    email = request.json['email']
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"message": "Email '%s' already registered" % email}), 409
    password = request.json['password']
    success, message = validate_password_strength(password)
    if not success:
        return jsonify({"message": message}), 400
    encrypted_password = cipher.encrypt(password)
    name = request.json['name']
    age = request.json['age']
    gender = request.json['gender']
    image = request.json['image']
    new_user = User(email, encrypted_password, name, age, gender, image)
    db.session.add(new_user)
    db.session.commit()
    return "", 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Data must be a JSON object"}), 400
    errors = login_form_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    decrypted_password = cipher.decrypt(user.password)
    if password == decrypted_password:
        expires = datetime.timedelta(minutes=app.config['TOKEN_EXPIRED_MIN'])
        identity = {
            'email': email,
            'password': password
        }
        access_token = create_access_token(identity=identity, expires_delta=expires)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Wrong password !"}), 401

@app.route("/api/auth/me", methods=["GET"])
@jwt_required
def show_me():
    me = get_jwt_identity()
    user = User.query.filter_by(email=me['email']).first()
    return user_schema.jsonify(user)

@app.route("/api/auth/reset-password", methods=["POST"])
def reset_password():
    if not request.is_json:
        return jsonify({"message": "Data must be a JSON object"}), 400
    errors = reset_password_schema.validate(request.json)
    if errors:
        return jsonify(errors), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    confirm = request.json.get('confirm', None)
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    if password != confirm:
        return jsonify({"message": "Password and confirm should be match"}), 400
    encrypted_password = cipher.encrypt(password)
    user.password = encrypted_password
    db.session.commit()
    return "", 204

@app.route("/api/auth/forgot-password", methods=["POST"])
def forgot_password():
    try:
        if not request.is_json:
            return jsonify({"message": "Data must be a JSON object"}), 400
        email = request.json.get('email', None)
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"message": "User not found"}), 404
        message = Message(
            subject='Reset your password',
            sender=app.config['MAIL_USERNAME'],
            recipients=[email],
            html = f"Need to reset your password?\n \
                    Just lick the button below and you'll be on your way.\n \
                    If you did not make this request, please ignore this email.\n \
                    <a href={url_for('reset_password')}>Reset Password</a>"
        )
        mail.send(message)
        return "Sent", 200
    except Exception as e:
        return jsonify(str(e)), 500

@jwt.unauthorized_loader
def unauthorized_loader(callback):
    return jsonify({
        'message': 'Missing `Authorization: Bearer <Access-Token>` Header'
    }), 401

@jwt.expired_token_loader
def expired_token_loader(callback):
    return jsonify({
        'message': 'Your Access-Token is expired. Please login again'
    }), 401


def main():
    app.run(host='0.0.0.0', port=app.config['APPLICATION_PORT'])
    
if __name__ == '__main__':
    main()
