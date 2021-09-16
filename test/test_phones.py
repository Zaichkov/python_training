from random import randrange
import re


def test_phones_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_details_page(app):
    index = randrange(app.contact.count())
    contact_from_details_page = app.contact.get_contact_from_details_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_details_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_details_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_details_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_details_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(clear,
                                filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.phone2]))))



