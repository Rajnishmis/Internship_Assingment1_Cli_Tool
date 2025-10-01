import unittest
from unittest.mock import patch
from client_validator.geo import fetch_geo_coordinates

class TestGeo(unittest.TestCase):
    @patch('client_validator.geo.requests.get')
    def test_fetch_geo_coordinates_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"lat": "-33.8688", "lon": "151.2093"}]
        result = fetch_geo_coordinates("Sydney, Australia")
        self.assertEqual(result, {"latitude": "-33.8688", "longitude": "151.2093"})

    @patch('client_validator.geo.requests.get')
    def test_fetch_geo_coordinates_no_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        result = fetch_geo_coordinates("Unknown Place")
        self.assertIsNone(result)

    @patch('client_validator.geo.requests.get')
    def test_fetch_geo_coordinates_error(self, mock_get):
        mock_get.side_effect = Exception("API error")
        result = fetch_geo_coordinates("Sydney, Australia")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
