from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def select_first_item(self):
        wd = self.wd
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            if field_name != "bday" and field_name != "bmonth" and field_name != "aday" and field_name != "amonth":
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def destroy(self):
        self.wd.quit()
