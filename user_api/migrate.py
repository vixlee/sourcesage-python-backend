from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from user_api.models import db
from user_api.app import app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
