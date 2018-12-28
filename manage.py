from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app, db, connect_to_db

migrate = Migrate(app, db)

manager = Manager(app)
connect_to_db(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':

    manager.run()