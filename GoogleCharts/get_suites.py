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

def get_suites(project_name):
    "Get the project ID using project name"
    client = get_testrail_client()
    project_id=get_project_id(project_name)
    print("Project ID:", project_id)
    suite_id = None
    suites = client.send_get('get_suites/%s' %project_id)
    # print(type(suites))
    df1 = pd.DataFrame(suites, columns = ['id','name','url'])
    # df1 = df1.columns(['name','id'])
    # print(df1)
    a = df1.columns.values.tolist()
    b = df1.values.tolist()
    # b.insert(0,a)
    # print(b)
    title = "Test Suites"
    tempdata = json.dumps({'title': a, 'data':b})
    return tempdata
    # df1.to_csv(r'C:\Users\4448\sample.csv', index= False)

# suite_data = get_suites('Project DELTA E2E')
# print(suite_data)