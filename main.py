from Word import Word
from Location import Location

first_location = Location(3, 5)
w1 = Word("zebra", "HR", first_location)
l2 = Location(-10, 10)
w2 = Word("Panther", "DLD", l2)
l3 = Location(2, 3)
w3 = Word("GIRAFFE", "DRU", l3)
print(w1)
print(w2)
print(w3)