import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="St_Claus"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="St_Claus"))
    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)

    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

