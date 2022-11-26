import re

class User():
    __firstname = ""
    __lastname = ""
    __email = "none"
    __website ="none"

    def __init__(self, firstname, lastname):
        self.__firstname =  firstname
        self.__lastname = lastname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        """  checks if the email address is valid by using a regex
        https://www.w3schools.com/python/python_regex.asp
        https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
                
        Args:
            value (str): the email to check
        """
        regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if(re.match(regex, value)):
            self.__email = value
        else:
            print("Invalid Email address")
        
    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, value):
        self.__website = value

    @property
    def fullname(self) -> str:
        """generates the full name of the user, based on the first and last name

        Returns:
            str: the full name of the user
        """
        return self.__firstname + " " + self.__lastname


def create_user() -> User:
    """Asks for input and returns a new user

    Returns:
        User: the user
    """
    firstname = get_input('first name')
    lastname = get_input('last name')
    email = get_input('email')
    website = get_input('website')
    user = User(firstname, lastname)
    user.email = email
    user.website = website
    return user


def add_user(user_list):
    """allows to add a user to the user list
    """
    person = create_user()
    user_list.append(person)
    print(f"{user_list[0].firstname} added")


def show_users(user_list: list):
    """Shows all users in the user list

    Args:
        user_list (list): the list with users
    """
    print('USERS:')
    print('')
    for user in user_list:
        print(f'user {user_list.index(user)}')
        print(f'full name: {user.fullname}')
        print(f'mail address: {user.email}')
        print(f'website: {user.website}')
        print('')


def get_input(text: str):
    """gets input

    Args:
        text (str): text that indicates which input is asked

    Returns:
        _type_: _description_
    """
    inp = input(f'Please enter {text}: ')
    return inp