import unittest
from client_validator.validation import is_blank, is_valid_email, validate_row
from client_validator.address_verification import is_valid_postcode, verify_address, validate_location_postcode

class TestValidation(unittest.TestCase):
    def test_is_blank(self):
        self.assertTrue(is_blank(""))
        self.assertTrue(is_blank(None))
        self.assertFalse(is_blank("abc"))

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("test@.com"))
        self.assertFalse(is_valid_email(""))

    def test_validate_row(self):
        row = {'email': '', 'first_name': '', 'last_name': '', 'residential_address': '', 'postal_address': ''}
        errors = validate_row(row)
        self.assertIn('Blank email', errors)
        self.assertIn('Blank first name', errors)
        self.assertIn('Blank last name', errors)
        self.assertIn('Blank residential address', errors)
        self.assertIn('Blank postal address', errors)

class TestAddressVerification(unittest.TestCase):
    def test_is_valid_postcode(self):
        self.assertTrue(is_valid_postcode('2000'))
        self.assertFalse(is_valid_postcode('abc'))
        self.assertFalse(is_valid_postcode('123'))

    def test_verify_address(self):
        self.assertTrue(verify_address('123 Main St', '2000'))
        self.assertFalse(verify_address('', '2000'))
        self.assertFalse(verify_address('123 Main St', 'abc'))

    def test_validate_location_postcode(self):
        row = {'residential_address': '123 Main St', 'residential_postcode': '2000', 'postal_address': '456 Side St', 'postal_postcode': '3000'}
        errors = validate_location_postcode(row)
        self.assertEqual(errors, [])
        row_invalid = {'residential_address': '', 'residential_postcode': 'abc', 'postal_address': '', 'postal_postcode': 'xyz'}
        errors = validate_location_postcode(row_invalid)
        self.assertIn('Invalid residential address/postcode', errors)
        self.assertIn('Invalid postal address/postcode', errors)

if __name__ == "__main__":
    unittest.main()
