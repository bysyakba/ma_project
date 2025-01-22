from routes.request import request

class RequestPutchEmail:
    URL = 'http://putch_email'

    def patch(emails, url=URL):
        file_path = 'file_path'
        try:
            old_email, new_email = emails
            response = request.post(new_email, write=False)
            if type(response) == tuple:
                with open(file_path, "r") as file:
                    lines = file.readlines()
                with open(file_path, "w") as file:
                    c = 404
                    for line in lines:
                        if line.strip() == old_email:
                            file.write(f'{new_email}\n')
                            c = 200
                        else:
                            file.write(line)
                    return c
            else:
                return 1337, 'Я индикатор некорректного емейла'
        except:
            return 400