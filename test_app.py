import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        response = self.app.post('/add', json={'num1': 5, 'num2': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

    def test_subtract(self):
        response = self.app.post('/subtract', json={'num1': 5, 'num2': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 2)

    def test_multiply(self):
        response = self.app.post('/multiply', json={'num1': 5, 'num2': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 15)

    def test_divide(self):
        response = self.app.post('/divide', json={'num1': 6, 'num2': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 2)

if __name__ == '__main__':
    unittest.main()
