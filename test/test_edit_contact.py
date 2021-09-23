from model.contact import Contact
import random


def test_edit_some_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="St_Claus"))
    old_contacts = orm.get_contact_list()
    contact_for_edit = random.choice(old_contacts)
    contact = Contact(firstname="edited_firstname", lastname="edited_lastname",
                      address="edited_address", mobile_phone="edited_phone", email="edited_email",
                      title="new_title", bday="19", bmonth="October", byear="1988", id=contact_for_edit.id)
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = orm.get_contact_list()
    old_contacts.remove(contact_for_edit)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        ui_list = app.contact.get_contact_list()
        orm_list = app.contact.make_list_like_ui(new_contacts)
        assert sorted(orm_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)
