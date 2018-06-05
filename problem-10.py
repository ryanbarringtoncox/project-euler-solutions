#!/usr/bin/python

upper_limit = 2000000

if __name__ == '__main__':

  # set defaults O(n) space
  prime_sorted_list = [True] * upper_limit 
  prime_sorted_list[0] = False
  prime_sorted_list[1] = False

  # filter out non-prime #s
  for curr_index in xrange(2, upper_limit): # O(n) time
    if prime_sorted_list[curr_index] == True:
      factor_counter = 1
      factor = curr_index
      while factor < upper_limit:
        factor_counter += 1
        factor = curr_index * factor_counter
        if factor < upper_limit:
          prime_sorted_list[factor] = False

  prime_sum = 0

  for idx, val in enumerate(prime_sorted_list): # O(n) time
    if val == True:
      prime_sum += idx

  print prime_sum
