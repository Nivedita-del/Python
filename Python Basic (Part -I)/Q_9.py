'''Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''
print("Enter the date")
a = input()
b = a.split(',')
print(b[0],'/',b[1],'/',b[2])