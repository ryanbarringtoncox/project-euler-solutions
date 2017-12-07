#!/usr/bin/python

'''
https://projecteuler.net/problem=21
'''

def get_divisors(x):
  '''returns a list of x's divisors'''
  divisors = []
  for i in range(1,x/2+1):
    if x % i == 0:
      divisors.append(i)
  return divisors

if __name__ == '__main__':

  amicable_pairs = [] # will hold all the amicable pairs
  
  for i in range(1,10000):

    # get i's divisors and sum them up
    divisors1 = get_divisors(i)
    sum_of_divisors1 = sum(divisors1)

    # get divisors of sum of i's divisors
    divisors2 = get_divisors(sum_of_divisors1)
    sum_of_divisors2 = sum(divisors2)

    # if second sum equals i and i isn't same as sum
    if i == sum_of_divisors2 and i != sum_of_divisors1:
      amicable_pairs.append(i)
      amicable_pairs.append(sum_of_divisors1)

  # filter out duplicates (aka make it a set) and sum
  amicable_set = set(amicable_pairs)
  print sum(amicable_set)
