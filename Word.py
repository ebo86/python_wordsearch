#Eboni Huggins
#Word Class


class Word:
    orientations = ['HR', 'HL', 'VD', 'VU', 'DRD', 'DLD', 'DLU']
    
    def __init__(self, word, orientation, location):
        self._word = word
        self._orientation = orientation
        self._location = location
        
    
    @property
    def word(self):
        return self._word

    @word.setter
    def word (self, word):
        self._word = word
    
    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        self._orientation = orientation
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        self._location = location
    
    
    def __str__(self):
        return ("{}".format(self.word))

