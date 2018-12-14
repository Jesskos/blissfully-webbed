from flask_sqlalchemy import SQLAlchemy

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
	guest_first_name = db.Column(db.String(40), nullable=False)
	guest_last_name = db.Column(db.String(40), nullable=False)
	guest_email = db.Column(db.String(40), nullable=True)
	guest_phone = db.Column(db.String(40), nullable=True)
	is_attending= db.Column(db.Boolean, nullable=False)

	def __repr__(self):
		return "<RSVP rsvp_id={} user_first_name={} user_last_name={} user_email={} user_phone={} attending={}>".format(self.rsvp_id, 
			self.guest_first_name, self.guest_last_name, self.guest_email, self.guest_phone, self.is_attending) 

def connect_to_db(app, uri='postgresql:///blissful_db'): # pragma: no cover
	""" Connect the database to our Flask App"""

	# Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = uri  
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  			
	db.app = app
	db.init_app(app)
	db.create_all()

if __name__ == "__main__":

	from server import app  # pragma: no cover
	connect_to_db(app)  # pragma: no cover
	print("Connected to DB.") # pragma: no cover


###########################################################################################################
# Testing   

def example_data():
	teddy = RSVP(user_first_name="teddy", user_last_name="koscheka", user_email="teddy@gmail.com", user_phone="5555555555", attending=True)
	trump = RSVP(user_first_name="donald", user_last_name="trump", user_email="dtrump@gmail.com", attending=False) 
	lucy = RSVP(user_first_name="lucy", user_last_name="koscheka", user_email="lucy@gmail.com", user_phone="5555555556", attending=True)
	db.session.add_all([teddy, trump, lucy])
	db.session.commit()