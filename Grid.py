###############################################################################
# Word Search (Grid class)
# Eboni Huggins
###############################################################################

# import libraries
from Location import Location
from Word import Word
from random import *



class Grid:
    
    BLANK = "."
    MAX_TRIES = 1000

    def __init__(self, size = 25):
        self._size = size
        self._grid = []
        self._words = []

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size 
    @property
    def grid(self):
        return self._grid
    
    @grid.setter
    def grid(self, grid):
        self._grid = grid 
    @property
    def words(self):
        return self._words      
    @words.setter
    def words (self, words):
        self._words= words
   

    def position(self, word, orientation): #location?
        min_row = 0
        max_row = self.size -1
        min_col = 0
        max_col = self.size -1

        # write the code that determines what changes then make the changes
        
        if (orientation == "HR") or (orientation == "DRD") or (orientation == "DRU"):
            max_col -= len(word)
        if (orientation == "HL") or (orientation == "DLD") or (orientation == "DLU"):
            min_col += len(word)-1
        if (orientation == "VD") or (orientation == "DRD") or (orientation == "DLD"):
            max_row -=len(word)
        if (orientation == "VU") or (orientation == "DLU") or (orientation == "DRU"):
            min_row += len(word)-1
        
        word = Word(word, orientation)  #added location


        # select a random location based on the min and max values
        loc = Location(randint(min_row, max_row), randint(min_col, max_col))   #############
        # check if this location works up to the specified maximum number of tries
        tries = 0
        while (not self._check(word, loc)):
            # stop trying if we've reached the specified maximum number of tries
            if (tries == Grid.MAX_TRIES):
                return 
            # select a new random location
            loc = Location(randint(min_row, max_row), randint(min_col, max_col))
            # note the attempt
            tries += 1

        # update the word's location
        word.location = loc
        
        # position the word in the grid at the location
        self._position(word)
        # and add it to the list of words
        self._words.append(word)
 

    # checks if a word can be positioned as specified
    def _check(self, word, loc):
        # the starting row and col for the word 
        row = loc.row
        col = loc.column
        
        # check if the word fits for the specified orientation
        for letter in word.word:   
            # abort if we don't encounter a space or the appropriate letter
            if (not self._grid[row][col] in [Grid.BLANK, letter]):
                return False  
            if (word.orientation == "HR") or (word.orientation == "DRD") or (word.orientation == "DRU"):
                col += 1
            if (word.orientation == "HL") or (word.orientation == "DLD") or (word.orientation == "DLU"):
                col -= 1
            if (word.orientation == "VD") or (word.orientation == "DRD") or (word.orientation == "DLD"):
                row +=1
            if (word.orientation == "VU") or (word.orientation == "DLU") or (word.orientation == "DRU"):
                row -=1
        return True

    # positions a word as specified
    def position(self, word):
        # the starting row and col for the word
        row = word.location.row 
        col = word.location.column 
      
        # position the word
        for letter in word.word:
            # place the current letter
            self._grid[row][col] = letter
            
            # so once again the row and/or column need to change (just like check)
            if (word.orientation == "HR") or (word.orientation == "DRD") or (word.orientation == "DRU"):
                col += 1
            if (word.orientation == "HL") or (word.orientation == "DLD") or (word.orientation == "DLU"):
                col -= 1
            if (word.orientation == "VD") or (word.orientation == "DRD") or (word.orientation == "DLD"):
                row +=1
            if (word.orientation == "VU") or (word.orientation == "DLU") or (word.orientation == "DRU"):
                row -=1
        
    # prints the words
    def print_words(self):
        wordSort = sorted(self.words)
        return wordSort
        
    # prints the solution
    def print_solution(self):
        return(self.__str__(False))

    # return a string representation of the grid
    def __str__(self, fill=True):
        grid = ""
        for row in range(self._size):
            for col in range(self._size):
                if (self._grid[row][col] == Grid.BLANK and fill):
                    grid += "{:2}".format(chr(randint(65, 90)))
                else:
                    grid += "{:2}".format(self._grid[row][col])
            grid += "\n"
        grid = grid.rstrip("\n")
        return grid