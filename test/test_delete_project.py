from model.project import Project
from random import randrange


def test_delete_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create_project(Project(name="Project_to_delete"))

    old_projects = app.project.get_projects_list()
    index = randrange(len(old_projects))

    app.project.delete_project(index)
    new_projects = app.project.get_projects_list()
    assert len(old_projects)-1 == len(new_projects)
