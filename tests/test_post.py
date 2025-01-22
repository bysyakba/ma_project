import pytest
from routes.request import request
from helpers.request_helper import email_exists_in_file, email_paparser, degenerate_url, invalid_degenerate_url
from constants import VALID_EMAILS
from conftest import delete_vaild_emails_file

class TestRequestPost:

    @pytest.mark.parametrize('url', email_paparser(degenerate_url()))
    def test_email_2valid(self, url, delete_vaild_emails_file):
        response = request.post(url)
        assert response[0] == 200
        assert email_exists_in_file(url)


    @pytest.mark.parametrize('url', email_paparser(degenerate_url()))
    def test_email_2valid(self, url, delete_vaild_emails_file):
        response = request.post(url)
        assert response[0] == 200
        assert email_exists_in_file(url)


    @pytest.mark.parametrize('invalid_degeneratbl', invalid_degenerate_url())
    def test_email_invalid(self, invalid_degeneratbl):
        response = email_paparser(invalid_degeneratbl)
        assert response == 404