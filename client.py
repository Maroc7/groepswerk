import re
import db
from inputs import get_input_item

class Client():
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
            self.__email = "n/a"
        
    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, value):
        if '.' in value:
            self.__website = value
        else:
            print('invalid website')
            self.__website = 'n/a'

    @property
    def fullname(self) -> str:
        """generates the full name of the user, based on the first and last name

        Returns:
            str: the full name of the user
        """
        return self.__firstname + " " + self.__lastname


def create_client() -> Client:
    """Asks for input and returns a new user

    Returns:
        User: the user
    """
    firstname = get_input_item('Give first name')
    lastname = get_input_item('Give last name')
    email = get_input_item('Give email')
    website = get_input_item('Give website')
    client = Client(firstname, lastname)
    client.email = email
    client.website = website
    return client


def add_client():
    """allows to add a user to the user list
    """
    client = create_client()
    try:
        sql_cmd = f"insert into t_client (f_firstname, f_lastname, f_mail, f_website) values ('{client.firstname}', '{client.lastname}', '{client.email}', '{client.website}');"
        db.cursor.execute(sql_cmd)
        db.connection.commit()
    except Exception as e:
        print(f'fout: {e}')


def show_clients():
    """show all clients
    """
    try:
        sql_cmd = 'select * from t_client;'
        db.cursor.execute(sql_cmd)
    
        rows = db.cursor.fetchall()
        print('-'*50)
        print('user ID - firstname - lastname - mail - website')
        print('-'*50)
        if len(rows) > 0:
            for row in rows:
                for i in row:
                    print(i, end=' - ')
                print('')
        else:
            print('geen gegevens gevonden')    
    except Exception as e:
        print(f'fout: {e}')
  

def delete_client():
    """deletes client
    """
    show_clients()
    inp = get_input_item("Select client id to delete", 1)
    check = get_input_item(f'WARNING: Delete is irreversible, enter "y" if you wish to delete user {inp}?')
    if check.strip().lower() == "y":
        try:
            sql_cmd = f'delete from t_client where pk_id = {inp};'
            db.cursor.execute(sql_cmd)
            db.connection.commit()
            print('Client deleted') 
        except Exception as e:
            print(f'fout: {e}')
    else:
        print('Nothing was deleted.') 