'''Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''

def charFreq(str_1):
    dict={}
    for i in str_1:
        keys = dict.keys()
        if i in keys:
            dict[i]+=1
        else:
            dict[i] = 1
    return dict

print(charFreq('google.com'))