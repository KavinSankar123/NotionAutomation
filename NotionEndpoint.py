import requests
import json


class NotionEndpointClass:
    NOTION_TOKEN = "secret_r8968L5ZiQYxtUCAbd9tsRMsJIPC7wxRw71WuxseQlx"
    DATABASE_ID = "e0df044e59764cd1b2b7c6bf02338146"
    headers = {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    class_lookup = {192723: "NROSCI0080",
                    187123: "ECON0100",
                    186341: "CS1632",
                    186336: "CS1555",
                    186313: "CS1502"}

    def get_pages(self):
        url = f"https://api.notion.com/v1/databases/{self.DATABASE_ID}/query"

        page_size = 100
        payload = {"page_size": page_size}
        response = requests.post(url, json=payload, headers=self.headers)

        data = response.json()

        # Put data into a json file
        with open('db.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def prepare_data(self, assignment_data: list) -> list:
        colors = ["default", "gray", "brown",
                  "orange", "yellow", "green",
                  "blue", "purple", "pink", "red"]
        course_colors = {"CS1555": colors[5],
                         "CS1632": colors[4],
                         "CS1502": colors[6],
                         "NROSCI0080": colors[8],
                         "ECON0100": colors[3]}

        assignment_list = []  # --> contains multiple dictionaries (in json format) that contains assignment data

        for i in range(len(assignment_data)):
            course = self.class_lookup[assignment_data[i][0]]
            assig_name = assignment_data[i][1]
            start_date = assignment_data[i][2]
            is_marked = False

            assignment_info = [is_marked, [course, course_colors[course]], start_date, assig_name]

            data = {
                "parent": {"database_id": self.DATABASE_ID},
                "properties": {
                    "Status": {"checkbox": assignment_info[0]},
                    "Course": {"type": "multi_select",
                               "multi_select": [{"name": assignment_info[1][0], "color": assignment_info[1][1]}]},
                    "Date": {"date": {"start": assignment_info[2], "end": None, "time_zone": None}},
                    "AssignmentName": {"title": [{"text": {"content": assignment_info[3]}}]}
                }
            }

            assignment_list.append(data)

        return assignment_list

    def upload_assignment(self, new_page_data_list):

        create_url = 'https://api.notion.com/v1/pages'

        for i in range(len(new_page_data_list)):

            payload = json.dumps(new_page_data_list[i])
            res = requests.request("POST", create_url, headers=self.headers, data=payload)

            status_code = res.status_code

            if status_code == 200:
                print("Upload Status Code:", status_code, "--> SUCCESS")
            elif status_code == 400:
                print("Upload Status Code:", status_code, "--> FAILED")


# notion_endpoint = NotionEndpointClass()
#
# assig_data = notion_endpoint.prepare_data([["CS1502", "Assignment 1", "2023-05-28"]])
#
# notion_endpoint.upload_assignment(assig_data)
