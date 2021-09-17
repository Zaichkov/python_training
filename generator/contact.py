import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_email():
    return random_string(prefix="", maxlen=15) + "@gmail.com"


def random_phone(maxlen):
    return "".join([random.choice(string.digits + '-' + '(' + ')' + ' ') for _ in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 32))


def random_month():
    return random.choice(["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"])


def random_year():
    return str(random.randrange(1900, 2022))


test_data = [Contact(firstname="", lastname="", address="", email="", mobile_phone="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 30), email=random_email(), mobile_phone=random_phone(15),
            bday=random_day(), bmonth=random_month(), byear=random_year()) for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
