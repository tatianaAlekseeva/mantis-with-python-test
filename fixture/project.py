from model.project import Project
from utils import fill_field_by_name


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element("xpath", "//button[text()='Create New Project']").click()
        fill_field_by_name(self, "name", project.name)
        wd.find_element("xpath", "//input[@type='submit' and @value='Add Project']").click()
        wd.find_element("css selector", ".fa-puzzle-piece")
        self.project_cache = None

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element("link text", name).click()
        wd.find_element("xpath", "//*/text()[normalize-space(.)='Delete Project']/parent::*").click()
        wd.find_element("xpath", "//input[@value='Delete Project']").click()
        wd.find_element("css selector", ".fa-puzzle-piece")
        self.project_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element("link text", "Manage").click()
            wd.find_element("link text", "Projects").click()

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements("css selector", "tr > td> a"):
                text = element.text
                project_id = element.get_attribute("href").split("=")[1]
                self.project_cache.append(Project(name=text, project_id=project_id))
        return list(self.project_cache)