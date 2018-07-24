from data.project import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_new_project(app, project):
    old_projects = app.soap.get_projects_list()
    app.project.create_project(project)
    new_projects = app.soap.get_projects_list()
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)