from email_validator import email_validator
def test_email_validation():
	assert email_validator('juno@email.com') == True
	assert email_validator('juno@email@.com') == False