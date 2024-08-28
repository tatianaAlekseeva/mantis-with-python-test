import random
from generator.data_generators import random_string
from model.project import Project


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name=random_string(7)))
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)