# -*- coding: utf-8 -*-
from model.contact import Contact
import re


# @pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, json_contacts, orm, check_ui):
    contact = json_contacts
    old_contacts = orm.get_contact_list()
    app.contact.create(contact)
    new_contacts = orm.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        ui_list = app.contact.get_contact_list()
        orm_list = app.contact.make_list_like_ui(new_contacts)
        assert sorted(orm_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)

