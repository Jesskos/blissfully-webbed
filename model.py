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
	attending= db.Column(db.Boolean, nullable=False)

	def __repr__(self):
		return "<RSVP rsvp_id={} user_first_name={} user_last_name={} user_email={} user_phone={} attending={}>".format(self.rsvp, 
			self.user_first_name, self.user_last_name, self.user_email, self.user_phone, self.attend)   


def connect_to_db(app, uri='postgresql:///blissful_db'): # pragma: no cover
	""" Connect the database to our Flask App"""

	# Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = uri  
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # pragma: no cover
	app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
	db.app = app
	db.init_app(app)
	db.create_all()

if __name__ == "__main__":

	from server import app  # pragma: no cover
	connect_to_db(app)  # pragma: no cover
	print "Connected to DB."  # pragma: no cover
