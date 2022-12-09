from datetime import date, datetime, timedelta
from typing import Optional
from consts import DATE_FORMAT
from dateutil import relativedelta

class MyDateTime(): 

    def __init__(self, value: Optional[date] = None):
        if isinstance(value, date):        
            self.mydate = value
        else:
            self.mydate = datetime.now().date()
         
    @property
    def mydate(self) -> date:
        return self.__date
    
    @mydate.setter
    def mydate(self, value: date):
        if isinstance(value, date):
        # if value is not None and type(value) is date:
            self.__date = value
        else:
            raise Exception('mydate is none or incorrect type')
    
    @property
    def today(self) -> date:
        return self.__date

    def __str__(self) -> str:
        return self.as_text(self.mydate)
    
    def as_text(self, adate: Optional[date] = None) ->str:
        """convert a given date to a text reprensentation, if not supplied
           use internal val
        Args:
            adate (date): _description_
        Returns:
            str: return a date as d-m-y
        """
        date_to_use = adate
        if not isinstance(date_to_use, date):
            date_to_use = self.mydate
        
        return '{}'.format(date_to_use.strftime(DATE_FORMAT))