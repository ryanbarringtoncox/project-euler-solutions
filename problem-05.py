#!/usr/bin/python

# eliminates redundant factor division, just checks 11-19 
def divisible_by_range(curr_number):
  for x in xrange(11,20):
    if (curr_number % x) != 0:
      return False
  return True

if __name__ == '__main__':

  curr_number = 20

  # check multiples of 20 until answer is found
  while True:
    if divisible_by_range(curr_number):
      print curr_number
      break
    curr_number += 20
