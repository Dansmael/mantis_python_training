from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))


testdata= [Project(name=random_string("name", 10), description=random_string("discription", 10))]