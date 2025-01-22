import pytest
from routes.request import request
from routes.request_putch_email import RequestPutchEmail
from helpers.request_helper import email_exists_in_file, email_paparser, degenerate_url, invalid_degenerate_url
from constants import VALID_EMAILS, NEW_VALID_EMAILS, NEW_INVALID_EMAILS, CASE_ERROR
from conftest import delete_vaild_emails_file

class TestRequests:

    d = 0
    p = 0

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

    @pytest.mark.parametrize('emails', NEW_VALID_EMAILS)
    def test_putch_valid(self, emails, delete_vaild_emails_file):
        [request.post(y) for y in VALID_EMAILS]
        response = RequestPutchEmail.patch(emails)
        assert response == 200
        assert email_exists_in_file(NEW_VALID_EMAILS[TestRequests.d][1])
        assert not email_exists_in_file(NEW_VALID_EMAILS[TestRequests.d][0])
        TestRequests.d += 1

    @pytest.mark.parametrize('emails', NEW_INVALID_EMAILS)
    def test_putch_invalid(self, emails, delete_vaild_emails_file):
        [request.post(y) for y in VALID_EMAILS]
        response = RequestPutchEmail.patch(emails)
        assert response == CASE_ERROR.get(emails[0])
        assert not email_exists_in_file(NEW_INVALID_EMAILS[TestRequests.p][1])
        TestRequests.p += 1