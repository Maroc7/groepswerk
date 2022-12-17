import re
import db
from inputs import get_input_item

class User():
    __firstname = ""
    __lastname = ""
    __email = "none"
    __website ="none"

    def __init__(self, firstname: str, lastname: str):
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
        if "." in value and "@" in value:
            self.__email = value
        else:
            print("invalid email address")
            self.__email = "n/a"
        
    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, value: str):
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

    def write_user(self):
        """writes user to the database
        """
        try:
            sql_cmd = f"insert into t_user (f_firstname, f_lastname, f_mail, f_website) values ('{self.firstname}', '{self.lastname}', '{self.email}', '{self.website}');"
            db.cursor.execute(sql_cmd)
            db.connection.commit()
        except Exception as e:
            print(f'fout: {e}')

    @staticmethod
    def delete_user(inp: int):
        """delete user from database

        Args:
            inp (int): id nr of user to be deleted
        """
        try:
            sql_cmd = f'delete from t_user where pk_id = {inp};'
            db.cursor.execute(sql_cmd)
            db.connection.commit()
            print('User deleted') 
        except Exception as e:
            print(f'fout: {e}')

    @staticmethod
    def show_users(project_id = -1):
        """show all users
        """
        project_id = get_input_item("Enter -1 to show all users or enter project id n° to show project specific users", 1)
        try:
            if project_id == -1:
                sql_cmd = 'select * from t_user;'
            else:
                sql_cmd = f'select f_firstname from t_user \
                            inner join t_task on t_user.pk_id = t_task.fk_user_id \
                            inner join t_project on t_task.fk_project_id = t_project.pk_id \
                            where t_project.pk_id = {project_id};'
            db.cursor.execute(sql_cmd)
            rows = db.cursor.fetchall()
            print('-'*50)
            print('user ID - firstname - lastname - mail - website')
            print('-'*50)
            if len(rows) > 0:
                for row in rows:
                    print('| ', end='')
                    for i in row:
                        print(i, end=' | ')
                    print('')
            else:
                print('geen gegevens gevonden')    
        except Exception as e:
            print(f'fout: {e}')


def create_user() -> User:
    """Asks for input and returns a new user

    Returns:
        User: the user
    """
    firstname = get_input_item('Give first name')
    lastname = get_input_item('Give last name')
    email = get_input_item('Give email')
    website = get_input_item('Give website')
    user = User(firstname, lastname)
    user.email = email
    user.website = website
    return user


def add_user():
    """allows to add a user to the user list
    """
    user = create_user()
    user.write_user()
  

def delete_user():
    """asks user which id to delete, double checks with user if ok to delete and than calls method to delete user
    """
    User.show_users()
    inp = get_input_item("Select user id to delete", 1)
    check = get_input_item(f'WARNING: Delete is irreversible, enter "y" if you wish to delete user {inp}?')
    if check.strip().lower() == "y":
        User.delete_user(inp)
    else:
        print('No deletion was done.') 


