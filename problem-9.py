#!/usr/bin/python
'''
https://projecteuler.net/problem=9
'''

def get_triplet_product():

  sum = 1000
  a = 3
  while a <= sum - 2:
    for b in range(a+1, sum - a):
      c = 1000 - a - b
      triple = [a,b,c]
      if a*a + b*b == c*c:
        #print triple
        return a*b*c
    a = a + 1

if __name__ == '__main__':

  print get_triplet_product()
