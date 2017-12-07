#!/usr/bin/python

if __name__ == '__main__':

  answer = 0
  raw_num = 2 ** (1000)

  for i in str(raw_num):
    answer = answer + int(i)

  print answer
