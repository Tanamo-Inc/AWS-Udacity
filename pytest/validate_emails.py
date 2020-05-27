
# Define function email_validator with parameter email
def email_validator(email):
    """"Returns valid email
    """
    if email.count('@') != 0 and email.count('.') != 0:
        return True
    else:
        return False




# # Call the email_validator function
# email_validator('a@g.com')