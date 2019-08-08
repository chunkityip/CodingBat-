double_char 
#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  count=''
  for x in str:
    count+=x*2
  return count
-------------------------------------------------------------------------------------------------------------------------------------------
count_hi 
#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  count=0
  for x in range(len(str)-1):
    if str[x:x+2] == 'hi':
      count+=1
  return count
---------------------------------------------------------------------------------------------------------------------------------------------
cat_dog
#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  cat =0
  dog =0
  for x in range(len(str)):
    if str[x:x+3] =='cat':
      cat+=1
    elif str[x:x+3] =='dog':
      dog+=1
  return cat == dog 
-------------------------------------------------------------------------------------------------------------------------------------------
count_code 
#Return the number of times that the string "code" appears anywhere in the given string, 
#except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  count=0
  for x in range(0,len(str)-3):
    if str[x:x+2] == 'co' and str[x+3] =='e':
      count+=1
  return count
----------------------------------------------------------------------------------------------------------------------------------------
end_other 
#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
#Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  a=a.lower()
  b=b.lower()
  return (a.endswith(b) or b.endswith(a))
#The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
----------------------------------------------------------------------------------------------------------------------------------------
xyz_there 
#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
#So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  for x in range(len(str)):
    if str[x]!= '.' and str[x+1:x+4]=='xyz':
      return True
    elif str[0:3]=='xyz':
      return True
  return False
