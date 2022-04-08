import json
from operator import imod
import helper
import uuid
from pprint import pprint

print(">>>>>> Welcome to the system. Please register or login.😊😊 <<<<<<")
menu_options = {
    1: 'Register',
    2: 'Login',
    3: 'Exit'
}

user_data = {}
project_data = {}

####################################################################################

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

####################################################################################


def register():
    print(">>>>>> Please Fill Your Data💭 <<<<<<")
    while True:
        first_name = input('>> Please enter your first name: ')
        if not first_name.isalpha():
            continue
        else:
            user_data["first_name"] = first_name
        last_name = input('>> Please enter your last name: ')
        if not last_name.isalpha():
            continue
        else:
            user_data["last_name"] = last_name
        break
    while True:
        email = input('>> Please enter an email: ')
        if not helper.email_validator(email):
            print('>> Please enter a valid email.')
            continue
        else:
            user_data["email"] = email
        break
    while True:
        password = input('>> Please enter a password: ')
        confirm_password = input('>> Please confirm your password: ')
        if not helper.password_validator(password, confirm_password):
            print('>> Please enter the same password.')
            continue
        else:
            user_data["password"] = password
            user_data["confirm_password"] = confirm_password
        break
    while True:
        mobile_phone = input('>> Please enter your phone number: ')
        if not helper.phone_number_validator(mobile_phone):
            print('>> Please enter valid phone number')
            continue
        else:
            user_data["mobile_phone"] = mobile_phone
        break

    f = open("data.json", "r")
    data = json.load(f)
    data.append(user_data)

    user = open("data.json", "w")
    json.dump(data, user)
    user.close()

####################################################################################


def login():
    print('>> User Login <<')
    email = input(">> Please enter your email: ")
    password = input(">> Please enter your password: ")
    json_file = open("data.json")
    list = json.loads(json_file.read())
    for dict in list:
        if dict['email'] == email and dict['password'] == password:
            print(">>>>>> You logged in successfully😎😎 <<<<<<")
            while True:
                print('>>>>>>>>>>>>>>>*****<<<<<<<<<<<<<<<')
                print('>> Create Project - press (1)')
                print('>> View All Project - press (2)')
                print('>> Edit Projct - press (3)')
                print('>> Delete Project - Press (4)')
                print('>> Exit - press (5)')
                print('>>>>>>>>>>>>>>>*****<<<<<<<<<<<<<<<')
                user_choice = int(input('>> your choice: '))
                if user_choice == 1:
                    create_project(email)
                elif user_choice == 2:
                    list_projects(email)
                elif user_choice == 3:
                    edit_project(email)
                elif user_choice == 4:
                    delete_project(email)
                elif user_choice == 5:
                    exit()
    else:
        print(">>>>>> Invalid User😢 <<<<<<")
    json_file.close()

####################################################################################


def create_project(user_email):
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
                if not helper.time_validation(start_time):
                    start_time = None
                    continue

            end_time = input('>> project end time: ')
            if helper.time_validation(end_time) and start_time < end_time:
                break

        project_data["start_time"] = start_time
        project_data["end_time"] = end_time
        project_data["user_email"] = user_email
        project_data["id"] = str(uuid.uuid1())
        break
    f = open("project.json", "r")
    data = json.load(f)
    data.append(project_data)
    project = open("project.json", "w")
    json.dump(data, project)
    project.write("\n")
    print('>>>>>> Project Created Successfully...😎😎 <<<<<<')
    project.close()


def list_projects(user_email):
    f = open("project.json", "r")
    data = json.load(f)
    for project in data:
        if user_email == project['user_email']:
            pprint(project)
            print("\n")


def delete_project(user_email):
    project_id = input("Type Project ID: ")

    f = open("project.json", "r")
    data = json.load(f)
    data_original_length = len(data)

    for index, project in enumerate(data):
        if user_email == project['user_email'] and project_id == project['id']:
            data.pop(index)

    if(len(data) != data_original_length):
        f = open("project.json", "w")
        json.dump(data, f)
    else:
        print("Error!😡😡")


def edit_project(user_email):
    project_id = input("Type Project ID: ")

    f = open("project.json", "r")
    data = json.load(f)

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

                f = open("project.json", "w")
                json.dump(data, f)

        if authorized:
            break
    else:
        print("Error!😡😡")
####################################################################################


while True:
    print_menu()
    option = ''
    try:
        option = int(input('>> Enter your choice: '))
    except:
        print('>>>>>> Wrong input. Please enter a number. <<<<<<')
    if option == 1:
        register()
    elif option == 2:
        login()
    elif option == 3:
        break
    else:
        print('>>>>>> Invalid option. Please enter a number between 1 and 2. <<<<<<')
