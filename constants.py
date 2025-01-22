VALID_EMAILS = ["example@example.com", "user@domain.co.uk", "pavel@gmail.com", "a@b.c", "user@domain.c"]
INVALID_COUNT = [2, 11, 'a', '!', -5, 100, '4f', 2.5, True, None, '']
NEW_VALID_EMAILS = [("pavel@gmail.com", "ivan@anal.nedorogo"), ("user@domain.c", "vany-nezhnyiy@minet.net")]
NEW_INVALID_EMAILS = [("pavel@gmail.com", "ivananal.nedorogo"), ("user@domain.c", "vany-nezhnyiy@minet.net", "ufyuf@fyuf.uy"), ("nesosaniy@vankom.xuy", "vany-nezhnyiy@minet.net")]
CASE_ERROR = {"pavel@gmail.com" : (1337, "Я индикатор некорректного емейла") , "user@domain.c" : 400, "nesosaniy@vankom.xuy" : 404}