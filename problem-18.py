#!/usr/bin/python

'''
https://projecteuler.net/problem=18
'''

rows = """
3
7 4
2 4 6
8 5 9 3
"""

rows = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

strs = []
ints = []

if __name__ == '__main__':

  # loop through rows, create 2d list of strings
  for line in rows.split('\n'):
    l = line.split() 
    # add non-empty rows
    if len(l) > 0:
      strs.append(l)

  # convert str's to int's
  for l in strs:
    new_l = []
    for s in l:
      new_l.append(int(s))
    ints.append(new_l)

  # loop through from bottom to top
  for l in reversed(ints):
    curr_index = ints.index(l)
    if curr_index != 0: # if it's not the final/first row
      new_row = []
      for x in range(0,len(l)-1):
        if l[x] > l[x+1]:
          new_row.append(l[x]+ints[curr_index-1][x])
        else:
          new_row.append(l[x+1]+ints[curr_index-1][x])
      print new_row
      # replace next row with new_one
      ints[curr_index-1] = new_row

