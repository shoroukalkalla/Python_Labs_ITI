from database import DB
import re

#>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<#


class User:
    def __init__(self, data_path) -> None:
        self.db = DB()
        self.db.connect_with_data(data_path)

#########################################################

    def register(self):
        user_data = {}
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
            if not self.email_validator(email):
                print('>> Please enter a valid email.')
                continue
            else:
                user_data["email"] = email
            break
        while True:
            password = input('>> Please enter a password: ')
            confirm_password = input('>> Please confirm your password: ')
            if not self.password_validator(password, confirm_password):
                print('>> Please enter the same password.')
                continue
            else:
                user_data["password"] = password
                user_data["confirm_password"] = confirm_password
            break
        while True:
            mobile_phone = input('>> Please enter your phone number: ')
            if not self.phone_number_validator(mobile_phone):
                print('>> Please enter valid phone number')
                continue
            else:
                user_data["mobile_phone"] = mobile_phone
            break

        self.db.store_user_data(user_data)
#########################################################

    def login(self):
        print('>> User Login <<')
        email = input(">> Please enter your email: ")
        password = input(">> Please enter your password: ")
        list = self.db.get_user_data()
        for dict in list:
            if dict['email'] == email and dict['password'] == password:
                print(">>>>>> You logged in successfully😎😎 <<<<<<")
                return dict
        else:
            print(">>>>>> Invalid User😢 <<<<<<")
            return None
#########################################################

    @staticmethod
    def email_validator(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return True
        return False
#########################################################

    @staticmethod
    def password_validator(password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False
#########################################################

    @staticmethod
    def phone_number_validator(number):
        mobile_pattern = "^\+20[0125][0-9]{9}$"
        if len(number) > 7 and re.match(mobile_pattern, number):
            return True
        return None

