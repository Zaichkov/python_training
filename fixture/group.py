from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and wd.find_elements_by_name("new")):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_group_page()
        self.group_cache = None

    def fill_group_fields(self, group):
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.app.select_item_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.app.select_item_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()
        self.group_cache = None

    def edit_first_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_group_page()
        self.app.select_item_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("update").click()
        self.open_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def make_list_like_ui(self, group_list):
        return list(map(lambda g: Group(id=g.id, name=self.app.field_like_on_home_page(g.name)), group_list))
