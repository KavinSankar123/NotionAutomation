import requests
import json
import canvasapi
from canvasapi import Canvas

API_KEY = "13997~eArUCjMMW5nAPzDfpMDpr7eT2EP6Kif5vw3VJwWkUWwK45OwHd6CAc0TfUAwVJqE"
API_URL = "https://canvas.pitt.edu/api/v1"
headers = {'Authorization': 'Bearer 13997~eArUCjMMW5nAPzDfpMDpr7eT2EP6Kif5vw3VJwWkUWwK45OwHd6CAc0TfUAwVJqE'}


spring_2023_courses = {"NROSCI0080": "/courses/192723",
                       "ECON0100": "/courses/187123",
                       "CS1632": "/courses/186341",
                       "CS1555": "/courses/186336",
                       "CS1502": "/courses/186313"}


def print_assignments_for_course(assignment_list: list):
    for i in range(len(assignment_list)):
        if assignment_list[i]["due_at"] is not None:
            print(assignment_list[i]["name"])
            print(assignment_list[i]["due_at"])
            print("-----------")


def extract_assignment_info(assignment_list: list) -> list:
    info = []
    for i in range(len(assignment_list)):
        name = assignment_list[i]["name"]
        due_at = assignment_list[i]["due_at"][:10]
        info.append([name, due_at])
    return info


# neuro_assignments = requests.get(API_URL + spring_2023_courses["NROSCI0080"] + "/assignments?per_page=50", headers=headers).json()
# econ_assignments = requests.get(API_URL + spring_2023_courses["ECON0100"] + "/assignments?per_page=50", headers=headers).json()
# cs1632_assignments = requests.get(API_URL + spring_2023_courses["CS1632"] + "/assignments?per_page=50", headers=headers).json()
# cs1555_assignments = requests.get(API_URL + spring_2023_courses["CS1555"] + "/assignments?per_page=50", headers=headers).json()
cs1502_assignments = requests.get(API_URL + spring_2023_courses["CS1502"] + "/assignments?per_page=50", headers=headers).json()


x = extract_assignment_info(cs1502_assignments)


