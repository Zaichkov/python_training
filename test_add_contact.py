# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Sergey", lastname="Zaichkov", address="Gomel",
                                        email="blabla@gmail.com", mobile_phone="12345678",
                                        bday="20", bmonth="September", byear="1987",
                                        aday="14", amonth="June", ayear="2021"))
    app.logout()



