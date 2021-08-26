from selenium.webdriver.support.ui import Select
from model.contact import Contact


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
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
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

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.select_item_by_index(index)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

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
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)
