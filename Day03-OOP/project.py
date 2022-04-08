from operator import truediv
import uuid
from database import DB
import re
from pprint import pprint
#>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<#


class Project:
    def __init__(self, data_path) -> None:
        self.db = DB()
        self.db.connect_with_project(data_path)

#########################################################

    def create(self, user_email):
        project_data = {}
        while True:
            title = input('>> project title: ')
            project_data["title"] = title
            details = input('>> project details: ')
            project_data["details"] = details
            total = int(input('>> project total target: '))
            project_data["total"] = total
            start_time = None

            while True:
                if not start_time:
                    start_time = input('>> project start time: ')
                    if not self.time_validation(start_time):
                        start_time = None
                        continue

                end_time = input('>> project end time: ')
                if self.time_validation(end_time) and start_time < end_time:
                    break

            project_data["start_time"] = start_time
            project_data["end_time"] = end_time
            project_data["user_email"] = user_email
            project_data["id"] = str(uuid.uuid1())
            break

        data = self.db.get_project_data()
        data.append(project_data)
        self.db.project_store_data(data)
        print('>>>>>> Project Created Successfully...😎😎 <<<<<<')
#########################################################

    def list(self, user_email):
        data = self.db.get_project_data()
        for project in data:
            if user_email == project['user_email']:
                pprint(project)
                print("\n")
#########################################################

    def delete(self, user_email):
        project_id = input("Type Project ID: ")

        data = self.db.get_project_data()
        data_original_length = len(data)

        for index, project in enumerate(data):
            if user_email == project['user_email'] and project_id == project['id']:
                data.pop(index)

        if(len(data) != data_original_length):
            self.db.project_store_data(data)
        else:
            print("Error!😡😡")

#########################################################

    def edit(self, user_email):
        project_id = input("Type Project ID: ")

        data = self.db.get_project_data()

        choice = None
        authorized = False
        for index, project in enumerate(data):
            if user_email == project["user_email"] and project_id == project["id"]:
                authorized = True
                while not choice:
                    choice = input("""
                    Choose
                        1- Edit Title
                        2- Edit Details
                        3- Edit Total Target
                        4- Edit Start & End Time
                        5- Edit All
                        6- Exit
                                        :: """)

                    if choice is "1":
                        title = input("Type Title: ")
                        data[index]['title'] = title
                    elif choice is "2":
                        details = input("Type Details: ")
                        data[index]['details'] = details
                    elif choice is "3":
                        total_target = input("Type Total Target: ")
                        data[index]["total_target"] = total_target
                    elif choice is "4":
                        start_time = input("Type Start Time: ")
                        end_time = input("Type End Time: ")
                        data[index]["start_time"] = start_time
                        data[index]["end_time"] = end_time
                    elif choice is "5":
                        title = input("Type Title: ")
                        details = input("Type Details: ")
                        total_target = input("Type Total Target: ")
                        start_time = input("Type Start Time: ")
                        end_time = input("Type End Time: ")

                        data[index]["title"] = title
                        data[index]["details"] = details
                        data[index]["total_target"] = total_target
                        data[index]["start_time"] = start_time
                        data[index]["end_time"] = end_time

                    self.db.project_store_data(data)

            if authorized:
                break
        else:
            print("Error!😡😡")
#########################################################

    @staticmethod
    def time_validation(time):
        time_pattern = "^[0-9]{2}:[0-9]{2}$"
        return re.fullmatch(time_pattern, time)

