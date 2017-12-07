#!/usr/bin/python
'''
https://projecteuler.net/problem=7
'''

def is_prime(n):
  for x in range(2,int(n/2 + 1)):
    if n % x == 0:
      return False
  return True

if __name__ == '__main__':

  limit = 10001
  n = 2 #lowest prime
  primes = []

  while len(primes) <= limit - 1:
    if is_prime(n):
      primes.append(n)
    #print "Added " + str(len(primes)) + "th prime"
    n = n + 1

  #print primes
  print primes[-1]
