import pytest
from routes.request import request
from helpers.request_helper import email_exists_in_file
from constants import VALID_EMAILS

class TestRequestPost:
    
    @pytest.mark.parametrize('email', VALID_EMAILS)
    def test_email_valid(self, email, delete_vaild_emails_file):
        response = request.post(email)
        assert response == 200
        assert email_exists_in_file(email)