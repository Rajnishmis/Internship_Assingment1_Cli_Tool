# validation.py
import re


def is_blank(value):
    return not value or str(value).strip() == ""


def is_valid_email(email):
    if is_blank(email):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_row(row):
    errors = []
    # Use correct CSV column names
    if is_blank(row.get('Email')):
        errors.append('Blank email')
    elif not is_valid_email(row.get('Email')):
        errors.append('Invalid email')
    if is_blank(row.get('First Name')):
        errors.append('Blank first name')
    if is_blank(row.get('Last Name')):
        errors.append('Blank last name')
    if is_blank(row.get('Residential Address Street')):
        errors.append('Blank residential address street')
    if is_blank(row.get('Residential Address Locality')):
        errors.append('Blank residential address locality')
    if is_blank(row.get('Residential Address State')):
        errors.append('Blank residential address state')
    if is_blank(row.get('Residential Address Postcode')):
        errors.append('Blank residential address postcode')
    if is_blank(row.get('Postal Address Street')):
        errors.append('Blank postal address street')
    if is_blank(row.get('Postal Address Locality')):
        errors.append('Blank postal address locality')
    if is_blank(row.get('Postal Address State')):
        errors.append('Blank postal address state')
    if is_blank(row.get('Postal Address Postcode')):
        errors.append('Blank postal address postcode')
    return errors
