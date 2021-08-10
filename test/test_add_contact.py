# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Sergey", lastname="Zaichkov", address="Gomel",
                               email="blabla@gmail.com", mobile_phone="12345678",
                               bday="20", bmonth="September", byear="1987",
                               aday="14", amonth="June", ayear="2021"))
