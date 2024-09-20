import re

def validate_name(name):
    return re.match(r"^[A-Z][a-zA-Z]{2,}$", name)

def validate_zip(zip_code):
    return re.match(r"^\d{6}", zip_code)

def validate_phone(phone):
    return re.match(r"^\d{2} \d{10}$", phone)

def validate_email(email):
    return re.match( r'^[a-zA-Z0-9]+([._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', email)
