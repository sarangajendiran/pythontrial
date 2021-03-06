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


def merge_df():
    df1 = pd.DataFrame([[1,2,3],[2,2,3],[3,1,2],[4,0,0]], columns=['id','no1','no2'])
    df2 = pd.DataFrame([[1,22,333],[2,2222,31],[3,11,212],[4,1,21]], columns=['id','noA1','noA2'])
    import numpy as np
    df2 = pd.merge(df2, df1, on=['id'], how='right')
    print(df2)
    return df2


def get_result_run_id():
    "Get the project ID using project name"
    client = get_testrail_client()
    result = client.send_get('get_results_for_run/300')
    df1 = pd.DataFrame(result, columns=['id','test_id','status_id','defects','version'])
    # , columns=['id','test_id','status_id','defects','version','comment']
    file1 = df1.to_csv(r'C:\Users\4448\testresult1.csv', index= False)
    return df1

# get_result_run_id()

from atlassian import Jira
jira_instance = Jira(
    url = Conf_Reader.JIRA_URL,
    username = Conf_Reader.TESTRAIL_USER,
    password = Conf_Reader.TESTRAIL_PASSWORD,
)
results = jira_instance.jql("project = DE2E")
print("JIRA connected", results)