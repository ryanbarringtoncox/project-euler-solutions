#!/usr/bin/python

def is_palindrome(n):
  '''Returns true if n is palindromic number, else false'''
  n_string = str(n)
  for i in xrange(0,len(n_string)/2):
    if n_string[i] != n_string[-1 - i]:
      return False
  return True

if __name__ == '__main__':
  
  # generate a list of all 3-digit numbers - O(n) time and O(n) space
  triple_digit_numbers = []
  for i in xrange(999,99,-1):
    triple_digit_numbers.append(i)

  # generate a set of all products - O(n^2) time and O(n^2) space
  product_set = set()
  for x in triple_digit_numbers:
    for y in triple_digit_numbers:
      product_set.add(x*y)

  # sort products - O(n) space and O(nlogn) time
  sorted_products = sorted(product_set)

  # traverse sorted_products, high to low, find largest palindrome - O(n) time
  curr_product = None
  for i in xrange(len(sorted_products)-1, -1, -1):
    curr_product = sorted_products[i]
    if is_palindrome(curr_product):
      break

  print curr_product


