from generator.data_generators import random_string
from model.project import Project


def test_add_project(app):
    old_projects = app.soap.get_project_list()
    project = Project(name=random_string(7))
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    new_project_id = app.soap.get_project_id_by_name(project.name)
    old_projects.append(Project(new_project_id, project.name))
    assert sorted(old_projects) == sorted(new_projects)
