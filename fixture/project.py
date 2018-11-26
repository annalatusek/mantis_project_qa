from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_project_site(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("root")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # wd.find_element_by_xpath("//a[contains(text(), 'Manage Projects')]").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.go_to_manage_project_site()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath(text).click()

    # def inherit_global_yes_no(self, field_name):
    #     wd = self.app.wd
    #     wd.find_element_by_name(field_name).click()

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_dropdown_value("status", project.status) # ("//select[@name='status'], value=release)"
        # self.inherit_global_yes_no("inherit_global", project.inherit_global)
        self.change_dropdown_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    # def count(self):
    #     wd = self.app.wd
    #     self.open_group_page()
    #     return len(wd.find_elements_by_name("selected[]"))
    #
    #     project_cache = None
    #
    # def get_project_list(self):
    #     if self.project_cache is None:
    #         wd = self.app.wd
    #         self.open_group_page()
    #         self.group_cache = []
    #         for element in wd.find_elements_by_css_selector("span.group"):
    #             text = element.text
    #             id = element.find_element_by_name("selected[]").get_attribute("value")
    #             self.group_cache.append(Group(name=text, id=id))
    #     return list(self.group_cache)
