"""
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.
"""
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
def narcissistic(value):
  square = []
  n = len(str(value))
  sum = 0
  for x in str(value):
    square.append(int(x)**n)
  for x in square:
    sum+=int(x)
  if sum == value:
      return print(True)
  else:
      return print(False)

narcissistic(7)     #True, '7 is narcissistic
narcissistic(371)   #True, '371 is narcissistic
narcissistic(122)   #False, '122 is not narcissistic
narcissistic(4887)  #False, '4887 is not narcissistic