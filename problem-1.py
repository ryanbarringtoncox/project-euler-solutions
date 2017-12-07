#!/usr/bin/python

def is_multiple(x):
  '''Return True if x is a multiple of 3,5,6 or 9'''
  mults = [3,5,6,9]
  for n in mults:
    if x % n == 0:
      return True
  
def add_multiples(x):
  '''Add multples below x'''
  sum = 0
  for n in range(1,x):
    #print n
    if is_multiple(n):
      sum = sum + n
  return sum

if __name__ == "__main__":

  print "Sum of multiples of natural numbers below 10, divisible by 3,5,6,9..."
  print add_multiples(10)

  print "Sum of multiples of natural numbers below 1000, divisible by 3,5,6,9..."
  print add_multiples(1000)
