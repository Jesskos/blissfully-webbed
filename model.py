from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

class User(db.Model):

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_first_name = db.Column(db.String(40), nullable=False)
	user_last_name = db.Column(db.String(40), nullable=False)
	user_type = db.Column(db.Integer, nullable=True)



class RSVP(db.Model):
	__tablename__ = "rsvps"

	rsvp_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_first_name = db.Column(db.String(40), nullable=False)
	user_last_name = db.Column(db.String(40), nullable=False)
	user_email = db.Column(db.String(40), nullable=True)
	user_phone = db.Column(db.String(40), nullable=True)
	attending? = db.Column(db.Boolean, nullable=False)



