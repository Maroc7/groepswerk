from datetime import date, datetime
C_DATEFORMAT = '%d/%m/%y'
C_CONTINUE_CHAR = "y"

class Task():
    _name = ""
    _startdate = ""
    _enddate = ""
    _status = ""


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


def get_input(text) -> str:
    inp = input(text)
    return inp


def create_task() -> str:
    task = Task()
    name = get_input("Give the name of task: ")
    startdate = get_input("Give the start date of task, {}: ".format(C_DATEFORMAT))
    enddate = get_input("Give end date of task, {}: ".format(C_DATEFORMAT))
    status = input("Give the status of the task: ")
    task._name = name
    task._startdate = startdate
    task._enddate = enddate
    task._status = status
    return task

def create_tasks() -> list:
    tasks = []
    
    choice = C_CONTINUE_CHAR
    while choice == C_CONTINUE_CHAR:
        task = create_task()
        tasks.append(task)
        choice = get_input("Do you want to add another task (y, any other character to stop.)".lower())

    return tasks


def print_all(tasks):
    for task in tasks:
        print("Task name : {}".format(task._name))
        print("start date: {}".format(task._startdate))
        print("end date : {}".format(task._enddate))
        print("status : {}".format(task._status))


def do_all():
    tasks = create_tasks()
    print_all(tasks)



