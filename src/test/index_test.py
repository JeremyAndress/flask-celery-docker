import unittest
from app import create_app

class RoutesApiTest(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def test_successful_service(self):
        print('here')