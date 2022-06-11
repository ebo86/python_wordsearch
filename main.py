from Word import Word
from Location import Location
from random import *




class getWord:                     
    lines = []
    myFile = open("animals.txt", "r")
    currentLine = myFile.readline()
    while currentLine:
        currentLine = currentLine.rstrip("\n")
        currentLine = currentLine.upper()
        lines.append(currentLine)
        currentLine = myFile.readline()
        return random.choices(lines, NUM_WORDS)

NUM_WORDS = 5
GRID_SIZE = 15
allWords = []
word_objects = []

for w in words:
    orientation = choice(Word.ORIENTATIONS)
    row = randint(0, GRID_SIZE - 1)
    col = randint(0, GRID_SIZE - 1)
    location = Location(row, col)
    word_objects.append(Word(w, orientation, location))
    grid.position(w, orientation)
    words = sample(allWords, NUM_WORDS)
    grid = Grid(GRID_SIZE) 

    # display the words
for w in word_objects:
    print(w)
    


totalWords = len(grid.words)

print(f"Successfully placed {totalWords} of {NUM_WORDS} words.\n")
print(grid, "\n")

for i in grid.print_words():
    print(i)

input("\nPress enter to see solution.\n")
print(grid.print_solution())
quit()






#from Word import Word
#from Location import Location

#first_location = Location(3, 5)
#w1 = Word("zebra", "HR", first_location)
#l2 = Location(-10, 10)
#w2 = Word("Panther", "DLD", l2)
#l3 = Location(2, 3)
#w3 = Word("GIRAFFE", "DRU", l3)
#print(w1)
#print(w2)
#print(w3)
