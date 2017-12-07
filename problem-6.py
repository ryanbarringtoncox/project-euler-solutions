#!/usr/bin/python
'''
https://projecteuler.net/problem=6
'''

if __name__ == '__main__':

  x = 100
  sum = 0
  sum_of_squares = 0

  for n in range(1, 101):
    sum = sum + n
    sum_of_squares = sum_of_squares + (n * n)

  square_of_sums = sum * sum

  print "sum_of_squares is " + str(sum_of_squares)
  print "square_of_sums is " + str(square_of_sums)
  print "difference is " + str(square_of_sums - sum_of_squares)
