'''Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java'''
print("Enter file name")
a = input()
b = a.split('.')
print(b[-1])