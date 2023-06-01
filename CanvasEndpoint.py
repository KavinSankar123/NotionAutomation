import requests

from NotionEndpoint import NotionEndpointClass


class CanvasEndpointClass:
    API_KEY = "[deleted it since this is a public repo]"
    API_URL = "https://canvas.pitt.edu/api/v1"
    headers = {'Authorization': 'Bearer <enter API key here>'}

    class_schedule = {"NROSCI0080": "/courses/192723",
                      "ECON0100": "/courses/187123",
                      "CS1632": "/courses/186341",
                      "CS1555": "/courses/186336",
                      "CS1502": "/courses/186313"}

    spring_2023_courses2 = {"NROSCI0080": "/courses/192723",
                            "CS1502": "/courses/186313"}

    def extract_assignment_info(self, assignment_list: list) -> list:
        info = []
        for i in range(len(assignment_list)):
            if assignment_list[i]["due_at"] is not None:
                course_id = assignment_list[i]["course_id"]
                name = assignment_list[i]["name"]
                due_at = assignment_list[i]["due_at"][:10]
                info.append([course_id, name, due_at])
        return info

    # Uses the dictionary with only 2 classes (spring_2023_courses2)
    def get_assignments(self) -> list:
        all_class_assignments = []
        for course in self.spring_2023_courses2:
            course_assignments = requests.get(self.API_URL +
                                              self.spring_2023_courses2[course] +
                                              "/assignments?per_page=50", headers=self.headers).json()

            trimmed_down_course_data = self.extract_assignment_info(course_assignments)
            all_class_assignments.append(trimmed_down_course_data)

        return all_class_assignments

    def get_single_class_assignments(self) -> list:
        course = "CS1502"
        cs1502_assignments = requests.get(self.API_URL +
                                          self.class_schedule[course] +
                                          "/assignments?per_page=50", headers=self.headers).json()
        return cs1502_assignments
    
    
