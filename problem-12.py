#!/usr/bin/python
'''
https://projecteuler.net/problem=12
'''

def get_factor_list(n):
  '''take int, n, add return pretty string of its factors i.e. "1,2,3,6"'''
  if n == 1: return [1]
  factors = []
  for i in range(1, int(n**0.5)+1): # search up to square root
    if n % i == 0: #add both divisors
      factors.append(i) 
      factors.append(n/i)
  #add n to its factors list
  factors.append(n)
  return sorted(set(factors)) #sort list and cast to set to remove duplicates

if __name__ == '__main__':

  num = 0
  counter = 0
  while True: 
    counter = counter + 1
    num = num + counter
    #print str(num) + ":"
    factor_list = get_factor_list(num)
    #print factor_list
    if len(factor_list) > 500:
      break

  # final answer
  print num
