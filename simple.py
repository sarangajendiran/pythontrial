import dotenv,os,testrail
import Conf_Reader
import pandas as pd
import json
def get_testrail_client():
    "Get the TestRail account credentials from the Conf_Reader.py"
    #Get the TestRail Url
    testrail_url = Conf_Reader.TESTRAIL_URL
    client = testrail.APIClient(testrail_url)
    #Get and set the TestRail User and Password
    client.user = Conf_Reader.TESTRAIL_USER
    client.password = Conf_Reader.TESTRAIL_PASSWORD
    # print("Connected to TestRail")
    return client

def get_project_id(project_name):
    "Get the project ID using project name"
    client = get_testrail_client()
    project_id=None
    projects = client.send_get('get_projects')
    for project in projects:
        if project['name'] == project_name: 
            project_id = project['id']
            #project_found_flag=True
            break
    return project_id

def get_suites(project_name, suite_name):
    "Get the project ID using project name"
    client = get_testrail_client()
    project_id=get_project_id(project_name)
    print("Project ID:", project_id)
    suite_id = None
    Suites = client.send_get('get_suites/%s' %project_id)
    for suite in Suites:
        if suite['name'] == suite_name: 
            suite_id = suite['id']
            print("Suite ID:", suite_id)
            break
    return suite_id, project_id

def get_cases(project_name, suite_name):
    "Get the project ID using project name"
    client = get_testrail_client()
    suite_id, project_id = get_suites(project_name, suite_name)
    print("Suites for the project ID:", suite_id)
    cases = client.send_get('get_cases/%s&suite_id=%s' %(project_id,suite_id))
    file1 = open(r'C:\Users\4448\sample.txt', 'w')
    case = 1
    # file1.write(str(cases[0]['title']))
    # file1.write('\n')
    # file1.close()
    num_lines = len(cases)
    print(num_lines)
    for case in range(num_lines):
        file1.write(str(cases[case]['title']))
        case+=case
        file1.write('\n')
    file1.close()
    return cases

# cases = get_cases('Project DELTA E2E', '14.Security & Access Management')
