from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/login')
def log_in():
	return render_template("login.html")

@app.route('/signup')
def log_in():
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


if __name__ == '__main__':
	app.run()

