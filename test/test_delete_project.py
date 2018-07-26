from model.project import Project
from random import randrange


def test_delete_project(app):
    if len(app.soap.get_projects_list("administrator", "root")) == 0:
        app.project.create_project(Project(name="Project_to_delete"))

    old_projects = app.soap.get_projects_list("administrator", "root")
    index = randrange(len(old_projects))

    app.project.delete_project(index)
    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects)-1 == len(new_projects)
