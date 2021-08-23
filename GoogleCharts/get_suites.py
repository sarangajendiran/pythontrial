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

def get_cases(suite_id):
    "Get the project ID using project name"
    client = get_testrail_client()
    cases = client.send_get('get_cases/25&suite_id=%s' %suite_id)
    if suite_id == 138:
        file1 = open(r'C:\Users\4448\sample.txt', 'w')
        file1.write(str(cases))
        file1.close()
    total_cases = len(cases)
    return total_cases

def get_suites(project_name):
    "Get the project ID using project name"
    client = get_testrail_client()
    project_id=get_project_id(project_name)
    # print("Project ID:", project_id)
    suite_id = None
    suites = client.send_get('get_suites/%s' %project_id)
    df1 = pd.DataFrame(suites, columns = ['id','name'])
    df1['total_cases'] = df1.apply(lambda x: get_cases(x['id']), axis=1)
    test_cases = df1['total_cases'].sum()
    print("Total Test Cases created so far", test_cases)
    a = df1.columns.values.tolist()
    b = df1.values.tolist()
    tempdata = json.dumps({'title': a, 'data':b})
    # print(b)
    tempdata1 = get_runs()
    return tempdata, tempdata1
    # df1.to_csv(r'C:\Users\4448\sample.csv', index= False)

def get_runs():
    "Get the project ID using project name"
    client = get_testrail_client()
    reports = client.send_get('get_runs/25')
    # df2 = pd.DataFrame(reports)
    # file = df2.to_csv(r'C:\Users\4448\testrunsfull.csv', index= False)
    df1 = pd.DataFrame(reports, columns = ['name','passed_count', 'blocked_count', 'untested_count','retest_count','failed_count','custom_status1_count','custom_status3_count'])
    df1.rename(columns = {'name' : 'Test Runs Name','passed_count' : 'Passed', 'blocked_count' : 'Blocked', 'untested_count' : 'UnTested','retest_count' : 'Retested','failed_count': 'Failed','custom_status1_count': 'InProgress','custom_status3_count': 'Deferred'}, inplace= True)
    # print(df1)
    file = df1.to_csv(r'C:\Users\4448\testruns.csv', index= False)
    # print("File generated")
    a = df1.columns.values.tolist()
    b = df1.values.tolist()
    b.insert(0,a)
    # print(b)
    tempdata1 = json.dumps({'title': a, 'data':b})
    return tempdata1

# suite_data = get_suites('Project DELTA E2E')
# print(suite_data)