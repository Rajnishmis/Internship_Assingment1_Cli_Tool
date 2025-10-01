# address_verification.py
# This is a stub for address and postcode/location validation
# You can integrate with real APIs or use simple logic for demonstration
import re


def is_valid_postcode(postcode):
    # Example: Australian postcode (4 digits)
    return bool(re.match(r"^\d{4}$", str(postcode)))


def verify_address(address, postcode):
    if not address or not postcode:
        return False
    return is_valid_postcode(postcode)


def validate_location_postcode(row):
    # Checks for valid location/postcode pair using correct CSV column names
    residential_valid = verify_address(
        row.get('Residential Address Street'),
        row.get('Residential Address Postcode')
    )
    postal_valid = verify_address(
        row.get('Postal Address Street'),
        row.get('Postal Address Postcode')
    )
    errors = []
    if not residential_valid:
        errors.append('Invalid residential address/postcode')
    if not postal_valid:
        errors.append('Invalid postal address/postcode')
    return errors
