import json
import re

from suds.client import Client
from suds import WebFault
import xml.etree.ElementTree as ET

from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        with open('target.json', 'r') as file:
            data = json.load(file)
            username = data['testuser']['username']
            password = data['testuser']['password']
        client = Client("http://localhost/mantisbt-2.26.3/api/soap/mantisconnect.wsdl")
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
        with open('target.json', 'r') as file:
            data = json.load(file)
            username = data['testuser']['username']
            password = data['testuser']['password']
        client = Client("http://localhost/mantisbt-2.26.3/api/soap/mantisconnect.wsdl")
        try:
            project_id = client.service.mc_project_get_id_from_name(username, password, project_name)
            return project_id
        except WebFault as e:
            print(f"An error occurred while accessing the SOAP service: {e}")

