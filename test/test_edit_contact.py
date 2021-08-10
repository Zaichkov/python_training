from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="edited_firstname", lastname="edited_lastname",
                                           address="edited_address", mobile_phone="edited_phone", email="edited_email",
                                           title="new_title", bday="19", bmonth="October", byear="1988"))
