import json
from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        client, password, username = self.get_soap_client()
        try:
            projects_data = client.service.mc_projects_get_user_accessible(username, password)
            projects = []
            for project in projects_data:
                project_id = project.id
                project_name = project.name
                projects.append(Project(project_id, project_name))
            return projects
        except WebFault as e:
            print(f"An error occurred while accessing the SOAP service: {e}")

    def get_project_id_by_name(self, project_name):
        client, password, username = self.get_soap_client()
        try:
            project_id = client.service.mc_project_get_id_from_name(username, password, project_name)
            return project_id
        except WebFault as e:
            print(f"An error occurred while accessing the SOAP service: {e}")

    def get_soap_client(self):
        with open('target.json', 'r') as file:
            data = json.load(file)
            base_url = data['web']['baseUrl']
            username = data['testuser']['username']
            password = data['testuser']['password']
        resource_path = "api/soap/mantisconnect.wsdl"
        client = Client(f"{base_url}{resource_path}")
        return client, password, username
