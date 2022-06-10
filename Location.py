#Eboni Huggins
#Location Class


from random import *
 

class Location:
    def __init__(self, row, column):
        self._row = row
        self._column = column
    
    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        self._row = row
    
    @property
    def column(self):
        return self._column

    @row.setter
    def column(self, column):
        self._column = column
        
    def __str__(self):
        return "({},{})".format(self._row, self._column)
    

    
