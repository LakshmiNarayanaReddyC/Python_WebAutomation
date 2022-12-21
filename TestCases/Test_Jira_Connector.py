'''
Created on Oct 14, 2021

@author: kattupd
'''
from jira import JIRA
import json
import io
import base64
import pandas as pd
import csv
import time
import requests
import pyautogui
from .conftest import auth

class JiraConnector(object):
    """
    The JiraConnector object handles interaction with JIRA API Server
    """

    def __init__(self,auth):
        """
        Initializes values for the instantiation of the JiraConnector object.
        """
        self.jiraServer = 'http://atlassian.carcgl.com/'
        self.jiraProjkey = auth[2]
        # self.test_exec_key='CD-3'
        # self.issueIdOrKey = 'CD-6'
        self.jiraUser = auth[0]
        self.jiraPass = auth[1]
        self.msg = self.jiraUser + ":" + self.jiraPass
        self.authString = base64.b64encode(self.msg.encode('ascii')).decode('ascii')
        self.headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": 'Basic ' + self.authString,
        }

    def test_get_project_req(self):
        """
        To Fetch Requirements Info for required Project
        """
        get_issue_url = self.jiraServer + 'rest/api/2/search'

        req_payload = {
            "jql": "project = " + self.jiraProjkey + " AND issuetype = Requirement",
            "startAt": 0,
            "maxResults": 5,
            "fields": [
                "summary", "priority", "issuelinks"
            ]
        }

        req_name_list = []
        response = requests.post(get_issue_url, headers=self.headers, data=json.dumps(req_payload))
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            # print(output_data['issues'])
            for i in range(0, len(output_data['issues'])):
                # print(output_data['issues'][i])
                # print(output_data['issues'][i]['key'])
                # print(output_data['issues'][i]['fields']['summary'])
                # print(output_data['issues'][i]['fields']['priority']['name'])
                req_name_list.append(output_data['issues'][i]['fields']['summary'])

        print('List of Requirements for ' + str(self.jiraProjkey) + ' : ' + str(req_name_list))

    def test_get_project_epics(self):
        """
        To Fetch Epics Info for required Project
        """
        get_issue_url = self.jiraServer + 'rest/api/2/search'

        epics_payload = {
            "jql": "project = " + self.jiraProjkey + " AND issuetype = Epic",
            "startAt": 0,
            "maxResults": 5,
            "fields": [
                "summary", "priority", "issuelinks"
            ]
        }

        epic_name_list = []
        response = requests.post(get_issue_url, headers=self.headers, data=json.dumps(epics_payload))
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            # print(output_data['issues'])
            for i in range(0, len(output_data['issues'])):
                # print(output_data['issues'][i])
                # print(output_data['issues'][i]['key'])
                # print(output_data['issues'][i]['fields']['summary'])
                # print(output_data['issues'][i]['fields']['priority']['name'])
                epic_name_list.append(output_data['issues'][i]['fields']['summary'])

        print('List of Epics for ' + str(self.jiraProjkey) + ' : ' + str(epic_name_list))

    def get_project_userstories(self):
        """
        To Fetch User Stories Info for required Project
        """
        get_issue_url = self.jiraServer + 'rest/api/2/search'

        story_payload = {
            "jql": "project = " + self.jiraProjkey + " AND issuetype = Story",
            "startAt": 0,
            "maxResults": 5,
            "fields": [
                "summary", "priority", "status",
            ]
        }

        story_name_list = []
        response = requests.post(get_issue_url, headers=self.headers, data=json.dumps(story_payload))
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            # print(output_data['issues'])
            for i in range(0, len(output_data['issues'])):
                # print(output_data['issues'][i])
                # print(output_data['issues'][i]['key'])
                # print(output_data['issues'][i]['fields']['summary'])
                # print(output_data['issues'][i]['fields']['priority']['name'])
                # print(output_data['issues'][i]['fields']['status']['name'])
                # print(output_data['issues'][i]['fields']['status']['id'])
                story_name_list.append(output_data['issues'][i]['fields']['summary'])

        print('List of User Stories for ' + str(self.jiraProjkey) + ' : ' + str(story_name_list))

    def get_project_bugs(self):
        """
        To Fetch Bugs Info for required Project
        """
        get_issue_url = self.jiraServer + 'rest/api/2/search'

        bug_payload = {
            "jql": "project = " + self.jiraProjkey + " AND issuetype = Bug",
            "startAt": 0,
            "maxResults": 5,
            "fields": [
                "summary", "priority", "status",
            ]
        }

        bug_name_list = []
        response = requests.post(get_issue_url, headers=self.headers, data=json.dumps(bug_payload))
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            # print(output_data['issues'])
            for i in range(0, len(output_data['issues'])):
                # print(output_data['issues'][i])
                # print(output_data['issues'][i]['key'])
                # print(output_data['issues'][i]['fields']['summary'])
                # print(output_data['issues'][i]['fields']['priority']['name'])
                # print(output_data['issues'][i]['fields']['status']['name'])
                # print(output_data['issues'][i]['fields']['status']['id'])
                bug_name_list.append(output_data['issues'][i]['fields']['summary'])

        print('List of Bugs for ' + str(self.jiraProjkey) + ' : ' + str(bug_name_list))

    def post_epic_issue(self,ename,summary,desc):
        """
        To Create Epic Issue for required Project
        """
        post_issue_url = self.jiraServer + 'rest/api/2/issue'

        epic_info_list = []

        create_epic_payload = {
            "fields": {
                "project":
                    {
                        "key": self.jiraProjkey
                    },
                "customfield_10004": ename,
                "summary": summary,
                "description": desc,
                "issuetype": {
                    "name": "Epic"
                }
            }
        }
        response = requests.post(post_issue_url, headers=self.headers, data=json.dumps(create_epic_payload))
        print(response.status_code)
        if response.status_code == 201:
            print('Epic Issue Created Successfully')
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            epic_info_list.append(output_data['id'])
            epic_info_list.append(output_data['key'])

        print('Epic Issue Info for ' + str(self.jiraProjkey) + ' : ' + str(epic_info_list))

    def post_userstory_issue(self,summary,desc):
        """
        To Create User Story Issue for required Project
        """
        post_issue_url = self.jiraServer + 'rest/api/2/issue'

        userstory_info_list = []
        create_story_payload = {
            "fields": {
                "project": {
                    "key": self.jiraProjkey
                },
                "summary": summary,
                "description": desc,
                "issuetype": {
                    "name": "Story"
                }
            }
        }
        response = requests.post(post_issue_url, headers=self.headers, data=json.dumps(create_story_payload))
        print(response.status_code)
        if response.status_code == 201:
            print('User Story Issue Created Successfully')
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            userstory_info_list.append(output_data['id'])
            userstory_info_list.append(output_data['key'])

        print('User Story Issue Info for ' + str(self.jiraProjkey) + ' : ' + str(userstory_info_list))

    def post_bug_issue(self,summary,desc):
        """
        To Create Bug Issue for required Project
        """
        post_issue_url = self.jiraServer + 'rest/api/2/issue'
        # desc = desc

        bug_info_list = []

        create_bug_payload = {
            "fields": {
                "project":
                    {
                        "key": self.jiraProjkey
                    },
                "summary": summary,
                "description": desc,
                "issuetype": {
                    "name": "Bug"
                }
            }
        }
        response = requests.post(post_issue_url, headers=self.headers, data=json.dumps(create_bug_payload))
        print(response.status_code)
        if response.status_code == 201:
            print('Bug Issue Created Successfully')
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            bug_info_list.append(output_data['id'])
            bug_info_list.append(output_data['key'])

        print('Bug Issue Info for ' + str(self.jiraProjkey) + ' : ' + str(bug_info_list))

    def create_attachement(self, issuekey='', filepath=''):
        """
        #To Add Attachement for created Bug Issues for required Project
        """
        headers = {
            'X-Atlassian-Token': 'nocheck',
            'Authorization': 'Basic ' + self.authString,
        }

        filename = filepath
        issuekey = issuekey
        post_attachments_url = self.jiraServer + \
                               'rest/api/2/issue/' + str(issuekey) + '/attachments'

        # filename = 'TestResults.html'
        files = {'file': open(filename, 'rb')}
        response = requests.post(post_attachments_url, headers=headers, files=files)
        print(response.status_code)
        print(response.text)

    def get_generic_tests(self):
        """
        To Get the All Generic TestCase Issues from Jira and saved to .csv file .
        """
        get_issue_url = self.jiraServer + 'rest/api/2/search'

        tests_payload = {
            "jql": "project = CD AND issuetype = Test AND cf[13600] = Generic",
            "startAt": 0,
            "maxResults": 2,
            "fields": [
                "customfield_13603"
            ]
        }

        test_name_list = []
        test_file_name_list = []
        response = requests.post(get_issue_url, \
                                 headers=self.headers, data=json.dumps(tests_payload))
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            # print(output_data['issues'])
            # print(len(output_data['issues']))

            for i in range(0, len(output_data['issues'])):
                # print(output_data['issues'][i])
                test_name_list.append(output_data['issues'][i]['key'])
                # print(output_data['issues'][i]['key'])
                # print(output_data['issues'][i]['id'])
                # print(output_data['issues'][i]['fields']['customfield_13603'])
                test_file_name_list.append(output_data['issues'][i]['fields']['customfield_13603'])

        print('List of Generic Tests for ' + str(self.jiraProjkey) + ' : ' + str(test_name_list))

        # saving the status of all tests in a .csv file
        dfdict = {'TestName': test_name_list, 'FileName': test_file_name_list}
        writer = 'test_info.csv'
        df = pd.DataFrame(dfdict)
        df.to_csv(writer, header=True, columns=["TestName", "FileName"])
        # return test_name_list ,test_file_name_list

    def get_execution_tests(self):
        """
        To Get the TestCase Execution Status Info from Jira Xray API and saved to .csv file .
        """
        get_test_exec_url = self.jiraServer + \
                            'rest/raven/1.0/api/testexec/' + str(self.test_exec_key) + '/test'

        test_name_list = [];
        test_id_list = []
        response = requests.get(get_test_exec_url, headers=self.headers)
        print(response.status_code)
        if response.status_code == 200:
            print(response.text)
            output = response.text
            output_data = json.loads(output)

            # print (len(output_data))
            for i in range(0, len(output_data)):
                # print (i)
                # print(output_data[i]['id'])
                test_name_list.append(output_data[i]['key'])
                test_id_list.append(output_data[i]['id'])
            # print(output_data[i]['key'])

        print('List of Execution Tests Info for ' + str(self.jiraProjkey) + ' : ' + str(test_name_list))

        # saving the status of all tests in a .csv file
        dfdict = {'TestName': test_name_list, 'TestID': test_id_list}
        writer = 'test_exec_info.csv'
        df = pd.DataFrame(dfdict)
        df.to_csv(writer, header=True, columns=["TestName", "TestID"])

    def create_results_file(self):
        # Compare Two CSV Files and create Results File
        f1 = open('test_info.csv', 'r')
        f2 = open('test_exec_info.csv', 'r')
        f3 = open('results.csv', 'w', newline="")

        c1 = csv.reader(f1)
        c2 = csv.reader(f2)
        c3 = csv.writer(f3)

        masterlist = list(c2)
        # print(masterlist)
        for hosts_row in c1:
            row = 1
            found = False
            for master_row in masterlist:
                results_row = hosts_row
                if hosts_row[1] == master_row[1]:
                    results_row.append(master_row[2])
                    found = True
                    break
                row = row + 1

            if not found:
                results_row.append('NOT FOUND in master list')

            c3.writerow(results_row)

        f1.close()
        f2.close()
        f3.close()

    def final_results_file(self):

        f1 = open('results.csv', 'r')
        f2 = open('required_report.csv', 'r')
        f3 = open('update_results.csv', 'w', newline="")

        c1 = csv.reader(f1)
        c2 = csv.reader(f2)
        c3 = csv.writer(f3)

        masterlist = list(c2)
        # print(masterlist)

        for hosts_row in c1:
            row = 1
            found = False
            for master_row in masterlist:
                results_row = hosts_row
                if hosts_row[2] == master_row[1]:
                    # results_row.append('FOUND in master list (row ' + str(row) + ')')
                    results_row.append(master_row[2])
                    found = True
                    break
                row = row + 1

            if not found:
                results_row.append('NOT FOUND in master list')
            c3.writerow(results_row)

        f1.close()
        f2.close()
        f3.close()

    def get_failed_results_file(self):
        df = pd.read_csv('detailed_report.csv', usecols=['TESTCLASS', 'Status'])
        Failed_Report_List = []
        test_id = df.TESTCLASS.tolist()
        # print (test_id)
        test_status = df.Status.tolist()
        # print (test_status)

        for i, j in zip(test_id, test_status):
            testid = i
            status = j
            if status == 'FAIL':
                Failed_Report_List
                Failed_Report_List.append(testid)

        print(Failed_Report_List)

    def test_status_upload(self, filepath=''):
        df = pd.read_csv('update_results.csv', usecols=['TestID', 'Status'])
        # print (df)
        # See the keys
        # print (df.keys())
        # See content in 'FileName'
        # print (df.TestID)
        # print (df.Status)
        test_id = df.TestID.tolist()
        # print (names)
        test_status = df.Status.tolist()
        # print (status)
        for i, j in zip(test_id, test_status):
            testid = i
            status = j
            print(status)
            if status == 'PASS':
                update_test_exec_url = self.jiraServer + \
                                       'rest/raven/1.0/api/testrun/' + str(testid) + '/status?status=PASS'
                response = requests.put(update_test_exec_url, headers=self.headers)
                print(response.status_code)
                if response.status_code == 200:
                    print(response.text)
                    print('Test Cases ' + str(test_id) + ' Status as updated as Passed Sucessfully')
            elif status == 'FAIL':
                update_test_exec_url = self.jiraServer + \
                                       'rest/raven/1.0/api/testrun/' + str(testid) + '/status?status=FAIL'
                response = requests.put(update_test_exec_url, headers=self.headers)
                print(response.status_code)
                if response.status_code == 200:
                    print(response.text)
                    print('Test Cases ' + str(testid) + ' Status as updated as Failed Sucessfully')

                time.sleep(2)
                res = self.post_bug_issue(desc='Automation Test Fail: ' + str(testid))
                # print(res)
                time.sleep(5)
                # self.create_attachement(res[0],'TestResults.html')
                self.create_attachement(res[0], filepath)

    def csv_read(self,file):
        """
        To Read csv data
        """
        df = pd.read_csv(file)
        csv_data = []
        for ind in range(0, 4):
            csv_data.append(df.iloc[0, ind])
        return csv_data

    def post_userstory_issue_from_csv(self, li):
        """
        To Create User Story Issues for required Project, Issues are taken from the csv file
        """
        post_issue_url = self.jiraServer + 'rest/api/2/issue'

        userstory_info_list = []
        key_jira = str(li[0])
        summary_jira = str(li[1])
        description_jira = str(li[2])
        issuetype_jira = str(li[3])
        create_story_payload = {
            "fields": {
                "project": {
                    "key": key_jira
                },
                "summary": summary_jira,
                "description": description_jira,
                "issuetype": {
                    "name": issuetype_jira
                }
            }
        }
        response = requests.post(post_issue_url, headers=self.headers, data=json.dumps(create_story_payload))
        print(response.status_code)
        if response.status_code == 201:
            print('User Story Isssue Created Successfully')
            print(response.text)
            output = response.text
            output_data = json.loads(output)
            userstory_info_list.append(output_data['id'])
            userstory_info_list.append(output_data['key'])

        print('User Story Issue Info for ' + str(self.jiraProjkey) + ' : ' + str(userstory_info_list))

    def delete_issue_bulk(self):
        """
        To Read the project ids from csv file exported from jira and delete through this API
        """
        filename = open(r'C:\Users\koppulai\Downloads\Carrier JIRA 2022-09-27T13_35_46+0200.csv', errors='ignore')
        file = csv.DictReader(filename)
        issuekey = []
        for col in file:
            issuekey.append(col['Issue key'])
        print(issuekey)
        for id in issuekey:
            url = "http://atlassian.carcgl.com/rest/api/2/issue/" + id
            response = requests.delete(url, headers=self.headers)
            print(response.text)
    # url = "https://your-domain.atlassian.net/rest/api/3/issue/{issueIdOrKey}"


# def jira_auth():
#     """
#     To Take authentication info from the user
#     """
#     auth=[]
#     print("Enter the username:")
#     username=pyautogui.prompt('Enter the username')
#     auth.append(username)
#     print("Enter the password")
#     password = pyautogui.password('Enter the password')
#     auth.append(password)
#     print("Enter the project key:")
#     auth.append(input())
#     return auth

def test_jira_operations(auth):
    """
    To perform the selected operation in jira
    """
    print("List of operations to be performed:\n 1. Get project requirements\n 2. Get project epics\n 3. Get project user stories\n 4. get project bugs\n 5. Get generic tests\n 6. Get execution tests\n 7. Get final results file\n 8. Get failed results file\n 9. Post epic issue\n 10. Post user story issue\n 11. Post bug issue\n 12. Post user story issues from csv\n 13. Create attachment\n 14. Upload test status\n 15. Delete Issues")
    yes = True
    while yes == True:
        print("Select a from the above listed operations by entering the corresponding number")
        menu = input()
        if menu == '1':
            JiraConnector(auth).test_get_project_req()
        elif menu == '2':
            JiraConnector(auth).test_get_project_epics()
        elif menu == '3':
            JiraConnector(auth).get_project_userstories()
        elif menu == '4':
            JiraConnector(auth).get_project_bugs()
        elif menu == '5':
            JiraConnector(auth).get_generic_tests()
        elif menu == '6':
            JiraConnector(auth).get_execution_tests()
        elif menu == '7':
            JiraConnector(auth).final_results_file()
        elif menu == '8':
            JiraConnector(auth).get_failed_results_file()
        elif menu == '9':
            print("Enter epic name:")
            ename = input()
            print("Enter Summary:")
            summary = input()
            print("Enter Description:")
            desc = input()
            JiraConnector(auth).post_epic_issue(ename,summary,desc)
        elif menu == '10':
            print("Enter Summary:")
            summary = input()
            print("Enter Description:")
            desc = input()
            JiraConnector(auth).post_userstory_issue(summary,desc)
        elif menu == '11':
            print("Enter Summary:")
            summary = input()
            print("Enter Description:")
            desc = input()
            JiraConnector(auth).post_bug_issue(summary,desc)
        elif menu == '12':
            li = []
            print("Enter the file path:")
            file=input()
            li = JiraConnector(auth).csv_read(file)
            JiraConnector(auth).post_userstory_issue_from_csv(li)
        elif menu == '13':
            JiraConnector(auth).create_attachement('CD-6','TestResults.html')
        elif menu == '14':
            JiraConnector(auth).test_status_upload()
        elif menu == '15':
            JiraConnector(auth).delete_issue_bulk()
        print("Do you want to continue performing operations:(y/n)")
        op=input()
        if (op == 'Y') or (op == 'y'):
            yes = True
        else:
            yes = False

# auth=jira_auth()
# test_jira_operations(auth)

"""
Upload test cases status info in excel sheet using in Jira Xray
"""
# obj = JiraConnector()
# obj.get_generic_tests()
# obj.get_execution_tests()
# obj.create_results_file()
# obj.final_results_file()
# obj.test_status_upload()
# lst = obj.get_failed_results_file()
# print(lst)
# obj.test_status_upload(filepath=lst[0])
