'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days '''
from datetime import date
from_date = date(2012,7,2)
to_date = date(2012,8,2)
temp = to_date - from_date
print(temp.days)