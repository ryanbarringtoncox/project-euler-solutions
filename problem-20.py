#!/usr/bin/python

def get_factorial(n):
  if n == 1:
    return n
  else:
    return n * get_factorial(n-1)

if __name__ == '__main__':

  # get the factorial
  x = get_factorial(100)

  # make it a string, slice it into single digits and add em up
  x = str(x)
  sum = 0
  for c in x:
   sum = sum + int(c) 
  print sum
