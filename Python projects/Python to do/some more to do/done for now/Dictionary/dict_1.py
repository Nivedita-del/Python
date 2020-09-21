fruit = {"orange" :"oranger in col",
         "apple" : "red in col",
         "lemon" : "yellow in col",
         "grape" : "purple in col",
         "lime": "very sour"}

print (fruit)
while True:
    dict_key = input("Please enter a fruit")
    if dict_key =="quit":
        break
    description = fruit.get(dict_key,"we dont have a "+dict_key)
    print(description)
