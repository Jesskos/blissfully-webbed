from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def welcome():
    pass

@app.route('/details')
def get_details():
	pass

app.route('/accommodations')
def get_accomodations():
	pass

@app.route('/story')
def get_story():
	pass

@app.route('/photos')
def view_photos():
	pass


@app.route('/registry')
def buy_buy_buy():
	pass

@app.route('/rsvp')
def rsvp():
	pass

@app.route('/message_board')
def view_message_board():
	pass


if __name__ == '__main__':
	app.run()

