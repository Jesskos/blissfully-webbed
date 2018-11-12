from unittest import TestCase
from server import app, rsvp_response
from model import db, example_data, RSVP, SQLAlchemy, connect_to_db

class FlaskTest(TestCase):

	def setUp(self):
		self.client = server.app.test_client()
		server.app.config['TESTING'] = True


		connect_to_db(app, "postgresql:///testdb")

		db.create_all()
		example_data()


	def tearDown(self):
		db.session.close()
		db.drop_all()

	def test_welcome(self):
		result = self.client.get('/')
		self.assertEqual(result.status_code, 200)
		self.assertIn('<body class="welcome-bg">', result.data)

	def test_rsvp(self):
		result = self.client.get('/rsvp')
		self.assertEqual(result.status_code, 200)
		self.assertIn('First Name: <input type="text" name="fname" id="first-name"><br>', result.data)

	def test_rsvp_form(self):
		result = self.client.post('/rsvp_response', 
			data={"first": "Brooke",
		"last": "Koscheka",
		"rsvp": "yes",
		"phone": "516-749-0527",
		"email": "bkoscheka@gmail.com", 
		"others": "1"})
		self.assertEqual(result.status_code, 200)
		self.assertIn("We have your RSVP! Cant's wait to see you", result.data)

	def test_rsvp_form(self):
		result = self.client.post('/rsvp_response', 
			data={"first": "teddy",
		"last": "koscheka",
		"rsvp": "yes",
		"phone": "516-749-0527",
		"email": "bkoscheka@gmail.com", 
		"others": "1"})
		self.assertEqual(result.status_code, 200)
		self.assertIn("You have already RSVPed!", result.data)







if __name__=='__main__':
	import unittest
	import server
	unittest.main()