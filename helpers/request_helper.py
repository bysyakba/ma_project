from routes.request_new_Email import RequestNewEmail
from constants import INVALID_COUNT
import random

def email_exists_in_file(email, file_path='valid_emails.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return email + '\n' in lines
    except FileNotFoundError:
       return False

def degenerate_url():
    BASE_URL = 'http://new_email_degenerator'
    return f'{BASE_URL}?count={random.randint(3, 10)}'

def invalid_degenerate_url():
    BASE_URL = 'http://new_email_degenerator'
    return [f'{BASE_URL}?count={x}' for x in INVALID_COUNT]

def email_paparser(url):
    respons = RequestNewEmail.get(url)
    try:
        if respons[0] == 200:
            return respons[1]
    except:
        return 404
   
