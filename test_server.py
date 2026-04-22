import unittest
import urllib.request

BASE_URL = "http://localhost:8000"

class TestHTTPServer(unittest.TestCase):

    def test_homepage(self):
        response = urllib.request.urlopen(BASE_URL)
        self.assertEqual(response.status, 200)

        html = response.read().decode('utf-8')
        self.assertIn("Python HTTP Server is Working", html)

    def test_index_file(self):
        response = urllib.request.urlopen(f"{BASE_URL}/index.html")
        self.assertEqual(response.status, 200)

if __name__ == "__main__":
    unittest.main()