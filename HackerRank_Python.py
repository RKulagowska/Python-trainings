# wydrukuj wszystkie kwadraty liczb dodatnich do podanej liczby n
#%

n = 5
for i in range(0,n):
    print(i**2)

# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
# otherwise return False
#%
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 ==0:
            leap = False
            if year % 400==0:
                leap = True
    return leap
        
year = 1990
print(is_leap(year))

# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:1,2,3...n
#%

n= 9
for i in range(1,n+1):
    print(i,sep =',',end='')

# You are given a string . Suppose a character '' occurs consecutively  times in the string. 
# Replace these consecutive occurrences of the character '' with  in the string.
# sample 1222311, output (1, 1) (3, 2) (1, 3) (2, 1)
#%
from itertools import groupby

string= '1223344556666777777'
print(' '.join( str( (len(list(g)), int(k)) ) for k,g in groupby(string)))