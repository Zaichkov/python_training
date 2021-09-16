# -*- coding: utf-8 -*-
import time

from model.contact import Contact
import pytest
import random
import string
import re


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


test_data = [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 30), email=random_email(), mobile_phone=random_phone(15),
            bday=random_day(), bmonth=random_month(), byear=random_year()),
    Contact(firstname=random_string("firstname", 15), lastname=random_string("lastname", 15),
            address=random_string("address", 40), email=random_email(), mobile_phone=random_phone(20),
            bday=random_day(), bmonth=random_month(), byear=random_year())
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    contact.firstname = field_like_on_home_page(contact.firstname)
    contact.lastname = field_like_on_home_page(contact.lastname)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def field_like_on_home_page(field):
    return re.sub(r'\s+', ' ', field).strip()
