from model.contact import Contact
import random


def test_delete_some_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="St_Claus"))

    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        ui_list = app.contact.get_contact_list()
        orm_list = app.contact.make_list_like_ui(new_contacts)
        assert sorted(orm_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)
