"""
Exercise:

Write one-liners that:

* produce a list with the length of each name
* produce a list with the first character of each name
* produce a list with all names having max 6 characters
* produce a dict with {name:length}
"""
from pprint import pprint
names = [
    'Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah', 
    'Alexis', 'Samantha', 'Jessica', 'Elizabeth', 'Taylor', 
    'Lauren', 'Alyssa', 'Kayla', 'Abigail', 'Brianna', 
    'Olivia', 'Emma', 'Megan', 'Grace', 'Victoria'
]
asc = {char: len(char) for char in names}
pprint(asc)
abc = {char: char for char in names}
pprint(abc)
