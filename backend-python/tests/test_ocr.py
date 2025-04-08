import unittest

from fastapi.testclient import TestClient
from app.main import app


class TestOCR(unittest.TestCase):

    def setUp(self):
        self.client  = TestClient(app)

    def test_upload(self):

        path = 'sample.txt'
        try:
            with open(path, 'rb') as image:
                response = self.client.post("/upload",files={"file": ("sample_image.png", image, "image/png")})
        except FileNotFoundError:
            print('')

        self.assertEqual(response.status_code, 200)
        self.assertIn("text", response.json())

if __name__ == "__main__":

    unittest.main()