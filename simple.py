import dotenv,os,testrail
import Conf_Reader
def get_testrail_client():
    
    "Get the TestRail account credentials from the testrail.env file"
    testrail_file = os.path.join(os.path.dirname(__file__),'testrail.env')
    #Get the TestRail Url
    testrail_url = Conf_Reader.TESTRAIL_URL
    client = testrail.APIClient(testrail_url)
    #Get and set the TestRail User and Password
    client.user = Conf_Reader.TESTRAIL_USER
    client.password = Conf_Reader.TESTRAIL_PASSWORD
    print("Connected to TestRail")
    return client
get_testrail_client()

