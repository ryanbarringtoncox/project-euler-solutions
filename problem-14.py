#!/usr/bin/python
'''
https://projecteuler.net/problem=14
'''

def collatz(n):
  if n % 2 == 0:
    return n/2
  else:
    return 3 * n + 1

if __name__ == '__main__':

  winner = 0
  largest_length = 0
  n = 0
  for i in range(1, 1000000):
  #for i in range(1, 10):
    seq = []
    seq.append(i)
    temp = i
    while temp != 1:
      seq.append(collatz(temp))
      temp = collatz(temp)
    #print "length of sequence is " + str(len(seq))
    if len(seq) > largest_length:
      largest_length = len(seq)
      winner = i

  print str(winner)
