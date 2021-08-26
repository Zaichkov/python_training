from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="St_Claus"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="edited_firstname", lastname="edited_lastname",
                      address="edited_address", mobile_phone="edited_phone", email="edited_email",
                      title="new_title", bday="19", bmonth="October", byear="1988", id=old_contacts[index].id)
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
