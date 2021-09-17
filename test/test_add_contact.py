# -*- coding: utf-8 -*-
from model.contact import Contact
import re


# @pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, json_contacts):
    contact = json_contacts
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
