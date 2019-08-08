count_evens 
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  count=0
  for num in nums:
    if num %2==0:
      count+=1
  return count
------------------------------------------------------------------------------------------------------------------------------------------
big_diff 
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
#Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(nums):
      return max(nums) - min(nums)
-------------------------------------------------------------------------------------------------------------------------------------------
centered_average 
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. 
#If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
#Use int division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(nums):
    small = min(nums)
    big = max(nums)
    return (sum(nums) - small - big) / (len(nums) - 2)
--------------------------------------------------------------------------------------------------------------------------------------------

