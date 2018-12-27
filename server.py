from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import connect_to_db,db, RSVP, GuestEmail
from jinja2 import StrictUndefined
import re

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

	print(request)
	# gets information from the form 
	first_name = request.form.get("first").lower()
	last_name = request.form.get("last").lower()
	rsvp_response = request.form.get("rsvp")
	phone_number = request.form.get("phone")
	email = request.form.get("email").lower()

	is_attending = (str(rsvp_response) == "yes")
	print("is_attending is {}".format(is_attending))


	#an empty dictionary to be sent out as JSON response to server
	response = {}

	#check to make sure user has not already RSVPed
	existing_rsvp = RSVP.query.filter(RSVP.guest_first_name==first_name, RSVP.guest_last_name==last_name).first()

	# checks if the guest already RSVPed, and if so, lets them know, adds them to the session, but does not modify db
	if existing_rsvp:
		print("existing rsvp)")
		response["message"] = "You have already RSVPed!"
		return jsonify(response)

	# if the rsvp does not exist, creates a new one and adds it to the database
	else:
		new_rsvp = RSVP(guest_first_name=first_name,
			guest_last_name=last_name,
			is_attending=is_attending, 
			guest_phone=phone_number, 
			guest_email=email)
		db.session.add(new_rsvp)
		db.session.commit()
		
		print(is_attending)

		if is_attending:
			response["message"] = "Your RSVP is now recorded. We look forward to seeing you"
		else:
			response["message"] = "Your RSVP is now recorded. Sorry you can't attend. We'll miss you"
		return jsonify(response)

@app.route('/submit_email', methods=["POST"])
def submit_email():

	response = {}
	guest_email = request.form.get("email")
	print "Submitting email {}".format(guest_email)
	if is_valid_email(guest_email):
		new_email = GuestEmail(email=guest_email)
		db.session.add(new_email)
		db.session.commit()
		response["message"] = "Thank you! We will notify you when the website is ready."

	else:
		response["message"] = "Please enter a valid email address"
	return jsonify(response)

		


############################################################################################################

def is_valid_email(email):
	if len(email) > 7 and re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
		return True 
	return False




if __name__ == '__main__':
	"***** Starting Server *****"
	connect_to_db(app)
	app.run(debug=True)
	

