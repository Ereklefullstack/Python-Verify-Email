from validate_email_address import validate_email

email = "example@example.com"
is_valid = validate_email(email, verify=True)
print(is_valid)  # True or False
