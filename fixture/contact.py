from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_css_selector('input[type="submit"]').click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_contact_fields(self, contact):
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middlename)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("nickname", contact.nickname)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home_phone)
        self.app.change_field_value("mobile", contact.mobile_phone)
        self.app.change_field_value("work", contact.work_phone)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)
        self.app.change_field_value("bday", contact.bday)
        self.app.change_field_value("bmonth", contact.bmonth)
        self.app.change_field_value("byear", contact.byear)
        self.app.change_field_value("aday", contact.aday)
        self.app.change_field_value("amonth", contact.amonth)
        self.app.change_field_value("ayear", contact.ayear)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.select_item_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(f"a[href='edit.php?id={id}']").click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("img[title='Details']")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def make_list_like_ui(self, contact_list):
        return list(map(lambda c: Contact(id=c.id, firstname=self.app.field_like_on_home_page(c.firstname),
                                          lastname=self.app.field_like_on_home_page(c.lastname),
                                          address=self.app.field_like_on_home_page(c.address),
                                          all_emails_from_home_page=self.merge_emails_like_on_home_page(c),
                                          all_phones_from_home_page=self.merge_phones_like_on_home_page(c)),
                        contact_list))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(map(self.app.field_like_on_home_page,
                             filter(lambda x: x is not None and x != "", [contact.email, contact.email2, contact.email3])))

    def merge_phones_like_on_home_page(self, contact):
        def clear(s):
            return re.sub("[() -]", "", s)
        return "\n".join(filter(lambda x: x != "",
                                map(clear,
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.phone2]))))

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_details_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        text = wd.find_element_by_id("content").text
        try:
            home_phone = re.search("H: (.*)", text).group(1)
        except AttributeError:
            home_phone = ""
        try:
            mobile_phone = re.search("M: (.*)", text).group(1)
        except AttributeError:
            mobile_phone = ""
        try:
            work_phone = re.search("W: (.*)", text).group(1)
        except AttributeError:
            work_phone = ""
        try:
            phone2 = re.search("P: (.*)", text).group(1)
        except AttributeError:
            phone2 = ""

        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)
