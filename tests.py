from unittest import TestCase
from server import app

class FlaskTest(TestCase):

	def setUp(self):
		self.client = server.app.test_client()
		server.app.config['TESTING'] = True

	# def tearDown(self):
	# 	db.session.close()
	# 	db.drop_all()

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
		self.assertIn("added", result.data)


if __name__=='__main__':
	import unittest
	import server
	unittest.main()