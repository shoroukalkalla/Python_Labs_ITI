from user import User
from project import Project

user = User("data.json")
project = Project("project.json")
#########################################################
print(">>>>>> Welcome to the system. Please register or login.😊😊 <<<<<<")
menu_options = {
    1: 'Register',
    2: 'Login',
    3: 'Exit'
}
#########################################################


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

#########################################################


def project_menu(email):
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
            project.create(email)
        elif user_choice == 2:
            project.list(email)
        elif user_choice == 3:
            project.edit(email)
        elif user_choice == 4:
            project.delete(email)
        elif user_choice == 5:
            exit()

#########################################################


while True:
    print_menu()
    option = ''
    try:
        option = int(input('>> Enter your choice: '))
    except:
        print('>>>>>> Wrong input. Please enter a number. <<<<<<')
    if option == 1:
        user.register()
    elif option == 2:
        logged_user = user.login()
        if logged_user:
            print("Hello", logged_user['first_name'])
            project_menu(logged_user['email'])
    elif option == 3:
        break
    else:
        print('>>>>>> Invalid option. Please enter a number between 1 and 2. <<<<<<')
