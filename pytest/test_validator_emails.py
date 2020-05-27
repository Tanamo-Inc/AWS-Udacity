from validate_emails import email_validator


# Test Passed
def test_email_passed():
    assert(email_validator('info@tanacom.io') == True)


# Test Failed
def test_email_failed():
    assert(email_validator('info@tancom') == True)
