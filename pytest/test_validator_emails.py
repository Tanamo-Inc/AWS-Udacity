from validate_emails import email_validator


#Test Passed 
def test_email():
    assert(email_validator('a@g.com')== True)
