people = {1:{'name': 'homes', 'age':'23','gender':'M'},
          2 :{'name': 'adler', 'age':'23','gender':'F'}}
print(people)

print(people[1]['name'])

people[3] = {}

people[3]['name']='Nivedita'
people[3]['age']='20'
people[3]['gender']='F'
people[3]['education']='btech'

print(people[3])

people[4] = {'name': 'homes', 'age':'23','gender':'M','Edu':'bcom'}

print(people[4])

del people[4]
print(people[4])
