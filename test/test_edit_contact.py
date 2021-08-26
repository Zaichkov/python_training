from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="St_Claus"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="edited_firstname", lastname="edited_lastname",
                      address="edited_address", mobile_phone="edited_phone", email="edited_email",
                      title="new_title", bday="19", bmonth="October", byear="1988", id=old_contacts[0].id)
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
