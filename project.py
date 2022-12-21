'''
id
projectnaam
beschrijving
firma
contactpersoon
datum aanvraag
vooropgestelde tijd
startdatum
einddatum
duur
'''
from mydatetime import MyDateTime
C_WIDTH_TEXT = 50

class Project():
    _proj_name = ''
    _description = ''
    enddate = ''

    def __init__(self, proj_name, description):
        self._proj_name = proj_name
        self._description = description

    @property
    def proj_name(self):
        return self._proj_name

    @proj_name.setter
    def proj_name(self,value):
        self._proj_name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,value):
        self._description = value


def get_input(text: str):
    inp = input(f'{text}: ')
    cnt = 1
    while len(inp) > C_WIDTH_TEXT * cnt:
        beg_substr = inp[:C_WIDTH_TEXT * cnt]
        end_substr = inp[C_WIDTH_TEXT * cnt:]
        inp = beg_substr + '\n' + end_substr
        cnt += 1
    return inp

def add_project(project: Project):
    project._proj_name = get_input('Geef de projectnaam:')
    project._description = get_input('Geef de projectbeschrijving')

def save_project():
    project = add_project()
    return project
