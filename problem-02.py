#!/usr/bin/python

def sum_fib(n):
  '''Sum first fib terms whose values do not exceed n'''

  #initial values
  x = 1
  y = 2

  #initial sum, set to x if doing even and odd numbers 
  sum = 0

  while y < n:
    temp = x
    x = y
    y = temp + x

    #only do even numbers
    if x % 2 == 0:
      sum = sum + x

  return sum

if __name__ == '__main__':
  print sum_fib(4000000)
