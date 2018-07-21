from model.project import Project
from data.project import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_new_project(app, project):
#    project = Project(name="New Project2", description="test")
    old_projects = app.project.get_projects_list()
    app.project.create_project(project)
    new_projects = app.project.get_projects_list()
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)