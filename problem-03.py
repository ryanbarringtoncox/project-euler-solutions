#!/usr/bin/python

def get_factors(n):
  '''returns set of factors of n'''
  factors = set()
  x = 2
  y = n/x
  while x <= y:
    if n % x == 0:
      factors.add(x)
      factors.add(y)
    x += 1
    y = n/x
  return factors

def get_largest_prime(factors):
  '''returns largest prime number in set'''

  largest_prime_factor = float("-inf")

  for factor in factors:
    if len(get_factors(factor)) == 0:
      if factor > largest_prime_factor:
        largest_prime_factor = factor
  
  return largest_prime_factor

if __name__ == '__main__':

  input = 600851475143
  factors = get_factors(600851475143)
  largest_prime_factor = get_largest_prime(factors)
  print "largest prime factor of " + str(input) + " is " + str(largest_prime_factor)
