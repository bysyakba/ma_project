from urllib.parse import urlparse, parse_qs
from faker import Faker

class RequestNewEmail:
    BASE_URL = 'http://new_email_degenerator'

    def get(url):

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        try:
            count = int(query_params['count'][0])
        except:
            return 404

        if count <= 2 or count >= 11:
            return 404

        fake = Faker()

        emails = [fake.email() for _ in range(count)]

        return 200, emails
