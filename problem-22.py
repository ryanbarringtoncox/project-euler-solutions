#!/usr/bin/python
import string

'''
https://projecteuler.net/problem=22
'''

# path to names file
file_path = ''

if __name__ == '__main__':

  # traverse filenames and add to list O(n) space, O(n) time
  names_list = []
  names = open(file_path).read()
  for name in names.split(','):
    names_list.append(name.replace('"',''))

  # sort the list alphabetically O(nlogn) time
  names_list = sorted(names_list)

  # work out alphabetical value for each name * position to get score O(n) time
  name_scores_total = 0
  counter = 1
  for name in names_list:
    letters_sum = 0
    for letter in name:
       letters_sum += string.uppercase.index(letter) + 1
    name_score = letters_sum * counter
    name_scores_total += name_score
    counter += 1

  # print total of name scores
  print name_scores_total
