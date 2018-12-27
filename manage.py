from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app
from model import db, connect_to_db


migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
	connect_to_db(app)
	manager.run()