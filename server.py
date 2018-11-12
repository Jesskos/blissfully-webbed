from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import connect_to_db,db, RSVP

app = Flask(__name__)

app.secret_key="Apple"

@app.route('/login')
def log_in():
	return render_template("login.html")

@app.route('/signup')
def sign_up():
	return render_template("signup.html")

@app.route('/')
def welcome():
    return render_template("welcome.html")	

@app.route('/details')
def get_details():
	return render_template("details.html")

@app.route('/hotels')
def get_accomodations():
	return render_template("hotels.html")

@app.route('/story')
def get_story():
	return render_template("story.html")

@app.route('/photos')
def view_photos():
	return render_template("photos.html")


@app.route('/registry')
def buy_buy_buy():
	return render_template("registry.html")

@app.route('/rsvp')
def rsvp():
	return render_template("rsvp.html")

@app.route('/message_board')
def view_message_board():
	return render_template("messageboard.html")

@app.route('/rsvp_response', methods=["POST"])
def rsvp_response():
	first_name = request.form.get("first").lower()
	last_name = request.form.get("last").lower()
	rsvp_response = request.form.get("rsvp")
	phone_number = request.form.get("phone")
	email = request.form.get("email").lower()
	other_guests = request.form.get("others")

	attending = (str(rsvp_response) == "yes")
	print "{} {} {} {} {} {} {}".format(first_name, last_name, rsvp_response, phone_number, email, other_guests, attending)

	#check to make sure user has not already RSVPed
	user_already_in_db = RSVP.query.filter(RSVP.user_first_name==first_name, RSVP.user_last_name==last_name).first()
	print user_already_in_db

	if user_already_in_db:
		return "You have already RSVPed! Can't wait to see you!"

	else:
		new_guest = RSVP(user_first_name=first_name,
			user_last_name=last_name,
			attending=attending, 
			user_phone=phone_number, 
			user_email=email)
		db.session.add(new_guest)
		db.session.commit()
		return "We have your RSVP! Cant's wait to see you"


if __name__ == '__main__':
	connect_to_db(app)
	app.run()
	

