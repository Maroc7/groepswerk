import inputs
import db
C_DATEFORMAT = '%d/%m/%y'
C_CONTINUE_CHAR = "y"

class Task():
    _name = ""
    _startdate = ""
    _enddate = ""
    _status = ""
    _responsible= ""
    _al_gestart= ""


def __init__(self,name):
    self._name = name

@property
def name(self):
    return self._name

@name.setter
def name(self,value):
    self._name = value

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
    """return birthdate with C_DATEFORMAT
    Returns:
    str: _enddate_
    """

    return self.enddate.strftime(C_DATEFORMAT)

enddate.setter
def enddate(self,value):
    self._enddate = value

@property
def status(self):
    return self._status

status.setter
def status(self,value):
    self._status = value

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




def create_task() -> str:
    task = Task()
    task._name = inputs.get_input_item("Give the name of task: ")
    task._startdate = do_startdate()
    task._enddate = do_enddate()
    task._responsible = inputs.get_input_item("Responsible: ")
    #task._al_gestart = inputs.get_input_item("Started?: ")

    task._status = inputs.get_input_item("Give status: ")
    return task

def create_tasks() -> list:
    tasks = []
    
    choice = C_CONTINUE_CHAR
    while choice == C_CONTINUE_CHAR:
        task = create_task()
        tasks.append(task)
        choice = inputs.get_input_item("Do you want to add another task (y, any other character to stop.)".lower())

    add_tasks(tasks)


def show_task():
    """show all tasks
    """
    try:
        sql_cmd = 'select * from f_task;'
        db.cursor.execute(sql_cmd)
    
        rows = db.cursor.fetchall()
        print('-'*50)
        print('task ID - name - startdate - enddate - status')
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



def delete_task():
    """deletes task
    """
    show_task()
    inp = inputs.get_input_item("Select task id to delete", 1)
    check = inputs.get_input_item(f'WARNING: Delete is irreversible, enter "y" if you wish to delete user {inp}?')
    if check.strip().lower() == "y":
        try:
            sql_cmd = f'delete from f_task where pk_id = {inp};'
            db.cursor.execute(sql_cmd)
            db.connection.commit()
            print('Task deleted') 
        except Exception as e:
            print(f'fout: {e}')
    else:
        print('Nothing was deleted.') 



def add_tasks(tasks):
    for task in tasks:
        try:
            sql_cmd = f"insert into f_task (f_name,f_start_date,f_end_date,f_status) values ('{task._name}', '{task._startdate}', '{task._enddate}', '{task._status}');"
            db.cursor.execute(sql_cmd)
            db.connection.commit()
            print(f"Task {task._name} is saved succesfully in the database.")
        except Exception as e:
            print(f'fout: {e}')




