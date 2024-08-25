import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

