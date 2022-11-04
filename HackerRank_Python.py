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

# You are given three integers x,y and z representing the dimensions of a cuboid 
# along with an integer n. Print a list of all possible coordinates given by 
# (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.

x = 1
y = 1
z = 1
n = 2
 
res= [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(res)

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n])


# Given the participants' score sheet for your University Sports Day, you are 
# required to find the runner-up score. You are given n scores. Store them 
# in a list and find the score of the runner-up (2 place).
#%
n = 5
scores =[2,3,6,6,5] 
new = sorted(set(scores))
print(new[-2])

print(sorted(set(scores))[-2])

# You are given a string. Split the string on a " " (space) delimiter and join 
# using a - hyphen.

a = "this is a string"
x= a.replace(' ','-')
print(x)

