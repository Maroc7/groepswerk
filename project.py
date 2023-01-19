import inputs
import db
C_DATEFORMAT = '%d/%m/%y'
C_CONTINUE_CHAR = "y"

class Project():
    _name = ""
    _description = ""
    _startdate = ""
    _enddate = ""

def __init__(self,name):
    self._name = name

@property
def name(self):
    return self._name

@name.setter
def name(self,value):
    self._name = value

@property
def description(self):
    return self._description

@description.setter
def description(self,value):
    self._description = value


@property
def startdate(self) -> str:
    """return startdate with C_DATEFORMAT
        Returns:
        str: _startdate_
    """

    return self.startdate.strftime(C_DATEFORMAT)

@startdate.setter
def startdate(self,value):
    self._startdate = value

@property
def enddate(self) -> str:
    """return enddate with C_DATEFORMAT
    Returns:
    str: _enddate_
    """

    return self.enddate.strftime(C_DATEFORMAT)

@enddate.setter
def enddate(self,value):
    self._enddate = value


def do_startdate():
    #day
    startdate_day = int(inputs.get_input_item("Give the day for the startdate: ",1))
    while startdate_day == 0:
        print("Error, Give an int.")
        startdate_day = int(inputs.get_input_item("Give the day for the startdate: ",1))
    while startdate_day > 31:
        print("Error give a valid day in")
        startdate_day = int(inputs.get_input_item("Give the day for the startdate: ",1))

    #month
    startdate_month = inputs.get_input_item("Give the month for the startdate: ",1)
    while startdate_month == 0:
        print("Error, give an int")
        startdate_month = int(inputs.get_input_item("Give the month for the startdate: ",1))
    while startdate_month > 12 or startdate_month == 0:
        print("Error, give a valid month in")
        startdate_month = int(inputs.get_input_item("Give the month for the startdate: ",1))

    #year
    startdate_year = inputs.get_input_item("Give the year for the startdate: ",1)
    while startdate_year == 0:
        print("Error, give an int")
        startdate_year = inputs.get_input_item("Give the year for the startdate: ",1)

    startdate = f"{startdate_day}/{startdate_month}/{startdate_year}"

    return startdate

def do_enddate():
    # day
    enddate_day = inputs.get_input_item("Give day of enddate: ",1)
    while enddate_day == 0:
        print("Error, Give an int.")
        enddate_day = int(inputs.get_input_item("Give the day for the enddate: ",1))
    while enddate_day > 31:
        print("Error give a valid day in")
        enddate_day = int(inputs.get_input_item("Give the day for the enddate: ",1))


    #month
    enddate_month = inputs.get_input_item("Give the month for the enddate: ",1)
    while enddate_month == 0:
        print("Error, give an int")
        enddate_month = int(inputs.get_input_item("Give the month for the enddate: ",1))
    while enddate_month > 12 or enddate_month == 0:
        print("Error, give a valid month in")
        enddate_month = int(inputs.get_input_item("Give the month for the enddate: ",1))

    #year
    enddate_year = inputs.get_input_item("Give the year for the enddate: ",1)
    while enddate_year == 0:
        print("Error, give an int")
        enddate_year = inputs.get_input_item("Give the year for the enddate: ",1)

    enddate = f"{enddate_day}/{enddate_month}/{enddate_year}"
    return enddate



def create_project() -> str:
    project = Project()
    project._name = inputs.get_input_item("Give the project's name: ")
    project._startdate = do_startdate()
    project._enddate = do_enddate()
    project._description = inputs.get_input_text("Description: ")
    try:
        sql_cmd = f"insert into t_project (f_name, f_description, f_start_date, f_end_date) values ('{project._name}', '{project._description}', '{project._startdate}', '{project._enddate}');"
        db.cursor.execute(sql_cmd)
        db.connection.commit()
        print(f"Project: {Project._name} is saved succesfully in the database.")
    except Exception as e:
        print(f'fout: {e}')


def show_projects():
    """show all projects
    """
    try:
        sql_cmd = 'select * from t_project;'
        db.cursor.execute(sql_cmd)
    
        rows = db.cursor.fetchall()
        print('-'*50)
        print('project ID - name - description - startdate - enddate')
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
