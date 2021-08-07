from selenium.webdriver.support.ui import Select


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
        wd = self.app.wd
        self.app.open_home_page()
        self.app.select_first_item()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("img[title='Edit']").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
