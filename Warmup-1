Sleep_in 
 # They sleep in if it is not a weekday or They're on vacation.

def sleep_in(weekday, vacation):
  if weekday != True or vacation ==True:
    return True
  else:
    return False
-------------------------------------------------------------------------------------------------------------------------------------------

monkey_trouble 
#We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False
  
#Next version is shorter 
def monkey_trouble(a_smile, b_smile):
  return (a_smile == b_smile)

#The way I am doing is In python , return will always True if we didn't set anything inot return.
#Therefore, (a_smile == b_smile) means True and the return statement will pass.
-------------------------------------------------------------------------------------------------------------------------------------------
sum_double 
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  sum = a+b
  if a==b:
    sum = sum *2
  return sum
--------------------------------------------------------------------------------------------------------------------------------------
diff21 
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  if n<21:
    return 21-n
  else:
    return 2*(n-21)
 ---------------------------------------------------------------------------------------------------------------------------------------
parrot_trouble 
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    return (talking  and (hour <7 or hour>20))
 ---------------------------------------------------------------------------------------------------------------------------------------
makes10
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  return (a+b==10 or a==10 or b==10) 
-----------------------------------------------------------------------------------------------------------------------------------------
near_hundred 
#Given an int n, return True if it is within 10 of 100 or 200.
#Note: abs(num) computes the absolute value of a number. It returns the absolute value of a numbe.

def near_hundred(n):
  return ((abs(100-n)<=10) or (abs(200-n)<=10))
------------------------------------------------------------------------------------------------------------------------------------------
pos_neg 
#Given 2 int values, return True if one is negative and one is positive. 
#Except if the parameter "negative" is True, then return True only if both are negative.
#This is a solution from the webiste
  
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
 #This is my solution
 #^ means Sets each bit to 1 if only one of two bits is 1. In this case, either a <0  or b<0.
  return (a<0)^(b<0) if not negative else (a<0) and (b<0)
------------------------------------------------------------------------------------------------------------------------------------------
not_string 
#Given a string, return a new string where "not " has been added to the front. 
#However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if str[0:3] =='not':
    return str
  else:
    return ('not' + ' ' +str)
# The way I am doing it is using the potition of array [0:3]= not. If the array 0 to 2 have no 'not', add 'not'

------------------------------------------------------------------------------------------------------------------------------------------
missing_char 
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  x =str[:n]
  y=str[n+1:]
  return x +y 
-----------------------------------------------------------------------------------------------------------------------------------------
front_back 
#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) <= 1:
    return str
  
  x = str[-1]
  mid = str[1:-1]
  y = str[0]
  return (x + mid +y)
----------------------------------------------------------------------------------------------------------------------------------------
 front3 
#Given a string, we'll say that the front is the first 3 chars of the string. 
#If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
  return (str[0:3]*3)
