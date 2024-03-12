import random
class secret_number:
    def __init__(self, secret_num, attempts):
        self.secret_num = secret_num
        self.attempts = attempts

    def guess(self, number):
        self.attempts.append(number)
        if number < self.secret_num:
            response = "higher"
        elif number > self.secret_num:
            response = "lower"
        elif number == self.secret_num:
            response = f"You won after {len(self.attempts)} attempts"
        return response
