print("First git push")
print("Second commit")
import dotenv,os,testrail,Conf_Reader
 
def get_testrail_client():
    "Get the TestRail account credentials from the testrail.env file"
    testrail_file = os.path.join(os.path.dirname(__file__),'testrail.env')
    #Get the TestRail Url
    testrail_url = Conf_Reader.get_value(testrail_file,'TESTRAIL_URL')
    client = testrail.APIClient(testrail_url)
    #Get and set the TestRail User and Password
    client.user = Conf_Reader.get_value(testrail_file,'TESTRAIL_USER')
    client.password = Conf_Reader.get_value(testrail_file,'TESTRAIL_PASSWORD')
    return client