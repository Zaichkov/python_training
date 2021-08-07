class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_fields(self, group):
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.app.select_first_item()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.app.select_first_item()
        wd.find_element_by_name("edit").click()
        self.fill_group_fields(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
