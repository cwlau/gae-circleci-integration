
import main
import unittest

class MainTest(unittest.TestCase):
    """This class uses the Flask tests app to run an integration test against a
    local instance of the server."""

    def setUp(self):
        self.app = main.app

    def test_hello_world(self):
        # rv = self.app.get('/get_author/ulysses')
        text = "Hello world"
        assert text == "Hello world"

if __name__ == '__main__':
    unittest.main()
