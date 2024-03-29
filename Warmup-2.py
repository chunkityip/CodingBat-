tring_times 
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  return (str * n)
----------------------------------------------------------------------------------------------------------------------------------------
front_times 
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. 
#Return n copies of the front;

def front_times(str, n):
  return (str[0:3] * n)
-----------------------------------------------------------------------------------------------------------------------------------------
string_bits 
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  show=""
  for x in range(len(str)):
    if x%2 ==0:
      show+=str[x]
  return show
----------------------------------------------------------------------------------------------------------------------------------------
string_splosion 
#Given a non-empty string like "Code" return a string like "CCoCodCode".def string_splosion(str):

def string_splosion(str):
 answer=''
  for x in range(len(str)):
    answer+=str[:x+1]
  return answer

# for the [:x+1], it means after 0.
#It likes 0:0+1, 0:1+1, 0:2+1................
---------------------------------------------------------------------------------------------------------------------------------------------
last2 
#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, 
#so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  last2 = str[len(str)-2:]
  answer = 0
  
  for i in range(len(str)-2):
    substring = str[i:i+2]
    if substring == last2:
      answer = answer + 1

  return answe
  ---------------------------------------------------------------------------------------------------------------------------------------------
array_count9 
#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  number =0
  for num in nums:
    if num ==9:
      number+=1
  return number
--------------------------------------------------------------------------------------------------------------------------------------
array_front9 
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
  for x in range(len(nums[0:3])):
    if nums[x]==9:
      return True
  return False
  ------------------------------------------------------------------------------------------------------------------------------------
array123 
#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  for x in range(len(nums)):
    if nums[x:x+3] == [1,2,3]:
      return True
  return False
  -------------------------------------------------------------------------------------------------------------------------------------
string_match 
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  count = 0

  for i in range(len(a)-1):
    for y in range(len(b)-1):
      a_sub = a[i:i+2]
      b_sub = b[y:y+2]
      if a_sub == b_sub:
        count += 1

  return count
  
  #second version
 
 def string_match(a, b):
  smallest = min(a,b) # To find out which string have shorter word.
  count = 0
  
  for i in range(len(smallest)-1):
    a_sub = a[i:i+2]
    b_sub = b[y:y+2]
    if a_sub == b_sub:
      count += 1
  return count
 -----------------------------------------------------------------------------------------------------------------------------
