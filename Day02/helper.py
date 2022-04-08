import re

# email validation:
def email_validator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
            return True
    return False

# password validation:
def password_validator(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False    

# phone number validation:
def phone_number_validator(number):
    mobile_pattern = "^\+20[0125][0-9]{9}$"
    if len(number) > 7 and re.match(mobile_pattern, number):
        return True
    return None

def time_validation(time):
    time_pattern = "^[0-9]{2}:[0-9]{2}$"
    return re.fullmatch(time_pattern, time)