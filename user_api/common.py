import base64
import hashlib
import os
import sqlite3
from Crypto import Random
from Crypto.Cipher import AES
import re

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def validate_password_strength(password):
    if len(password) < 8:
        return (False, "Password length is at least 8 characters")
    if not re.search(r'\d', password):
        return (False, "Password must contains at least one digit character")
    if not re.search(r'[A-Z]', password):
        return (False, "Password must contains at least uppercase character")
    if not re.search(r'[a-z]', password):
        return (False, "Password must contains at least lowercase character")
    if not re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password):
        return (False, "Password must contains at least special character")
    return (True, "")

def create_db_file(path_file):
    db = sqlite3.connect(path_file)
    db.execute('''
        CREATE TABLE user (
            id INTEGER NOT NULL, 
            email VARCHAR(120) NOT NULL, 
            password VARCHAR, 
            name VARCHAR(120), 
            age INTEGER, 
            gender INTEGER, 
            image VARCHAR, 
            PRIMARY KEY (id), 
            UNIQUE (email)
        );
    ''')
    db.close()
