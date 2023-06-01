import requests
import json

# New NOTION_TOKEN works BUT database ID doesn't work for some reason
NOTION_TOKEN = "secret_r8968L5ZiQYxtUCAbd9tsRMsJIPC7wxRw71WuxseQlx"
# DATABASE_ID = "937f05b6ed934d5a9c2914cb97fc5f05"

# Old token and ID from SheInnovates project
# NOTION_TOKEN = "secret_6i4uDnuWACqoVTiBsteKaUAXJ5RBqh6ZANauN4DdpON"
DATABASE_ID = "e0df044e59764cd1b2b7c6bf02338146"


headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    page_size = 100
    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Put data into a json file
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def prepare_data(assignment_data: list) -> dict:
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Status": {"checkbox": assignment_data[0]},
            "Due At": {"type": "multi_select", "multi_select": [{"name": assignment_data[1], "color": "red"}]},
            "Course": {"type": "multi_select",
                       "multi_select": [{"name": assignment_data[2][0], "color": assignment_data[2][1]}]},
            "Date": {"date": {"start": assignment_data[3], "end": None, "time_zone": None}},
            "Task": {"type": "multi_select",
                     "multi_select": [{"name": assignment_data[4][0], "color": assignment_data[4][1]}]},
            "AssignmentName": {"title": [{"text": {"content": assignment_data[5]}}]}
        }
    }

    return data


def upload_single_assignment(new_page_data):
    create_url = 'https://api.notion.com/v1/pages'

    payload = json.dumps(new_page_data)
    res = requests.request("POST", create_url, headers=headers, data=payload)

    status_code = res.status_code

    if status_code == 200:
        print("Upload Status Code:", status_code, "--> SUCCESS")
    elif status_code == 400:
        print("Upload Status Code:", status_code, "--> FAILED")


# ----------------Upload Data Variables------------------- #
# Multi Select colors
colors = ["default", "gray", "brown",
          "orange", "yellow", "green",
          "blue", "purple", "pink", "red"]

assignment_name = "CS1555 Homework"
course = "CS1555"
task = "Homework"
is_marked = False
start_date = "2023-05-28"
due_at_time = "11:59pm"

assignment_info = [is_marked, due_at_time, [course, colors[9]], start_date, [task, colors[6]], assignment_name]
upload_data = prepare_data(assignment_info)
upload_single_assignment(upload_data)

