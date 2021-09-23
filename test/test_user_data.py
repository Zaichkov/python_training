from model.contact import Contact


def test_data_on_home_page(app, orm):
    contacts_from_db = orm.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()

    assert sorted(app.contact.make_list_like_ui(contacts_from_db), key=Contact.id_or_max) ==\
           sorted(contacts_from_home_page, key=Contact.id_or_max)
