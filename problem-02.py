#!/usr/bin/python

def print_fib(n):
  '''print first n fib terms'''
  if n == 0: return

  x = 1
  print x
  if n == 1: return

  y = 2
  print y
  if n == 2: return

  count = 2
  while count < n:
    count = count + 1
    print x + y
    temp = x
    x = y
    y = temp + x

def sum_fib(n):
  '''sub first fib terms whose values do not exceed n'''

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
