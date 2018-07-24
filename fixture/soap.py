from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    soap_project_cache = None

    def get_projects_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        project_list = []
        try:
            client.service.mc_projects_get_user_accessible("administrator", "root")
            for project in client.service.mc_projects_get_user_accessible("administrator", "root"):
                project_list.append(Project(id=str(project['id']), name=project['name'], description=project['description']))
            return project_list
        except WebFault:
            return False

