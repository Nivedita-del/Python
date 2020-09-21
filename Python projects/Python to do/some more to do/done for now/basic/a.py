number = "9,2,342,445,654,234,3425"
cleanedNumber = ''
for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))
