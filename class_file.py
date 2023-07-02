from random import randint

symbols = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890_-+=*/|,.$@%^&<>()[]{}'

class Password:
    def __init__(self, count):
        self.count = count

    def logic(self):
        symbols_list = list(symbols)
        password = ''

        if self.count < 10 or self.count > 20:
            self.count = 10

        for i in range(0, self.count):
            password += symbols_list[randint(0, len(symbols_list))]
        return password