from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            # testing for routing to root
            self.assertEqual(response.status_code, 200)

            # Testing template #
            self.assertIn('Home Page', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:

            response = client.get('/api/new-game')

            #maybe to delete of them
            #implicitly testing if return is json

            #testing if we are getting a response
            assert any(response.get_json()) is not False

            #testing the response if it is a dictionary
            assert type(response.get_json()) is dict
            
            #testing if we are getting a list 
            assert type(response.get_json()["board"]) is list

            #testing if game id has been serialized
            assert type(response.get_json()["gameId"]) is str 
   
    def test_score_word(self):
        """Test word score"""

        with self.client as client:
            
            response = client.get('/api/score-word')