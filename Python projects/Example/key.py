people= {1:{'name': 'homes', 'age':'23','gender':'M'},
         2 :{'name': 'adler', 'age':'23','gender':'F'}}
for p_id, p_info in people.items():
    print("\n id",p_id)
 
    for key in p_info:
        print(key + ':',p_info[key])
