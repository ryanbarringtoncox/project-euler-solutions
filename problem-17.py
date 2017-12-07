#!/usr/bin/python

low_num_map = {
  0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9:'nine',
  10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19:'nineteen'
}

tens_map = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
}

def slice_first_digit(x):
  '''slices first digit off number i.e. 123 becomes 23'''
  return int(str(x)[1:])

def two_digits(x):
  #print "two_digits() called with " + str(x)
  if x < 20:
    return low_num_map[x]
  else:
    first_digit = str(x)[0]
    second_digit = str(x)[1]
    return tens_map[int(first_digit)] + " " + low_num_map[int(second_digit)]

def three_digits(x):
  first_digit = int(str(x)[0])
  other_digits = slice_first_digit(x)
  if other_digits == 0:
    return low_num_map[first_digit] + " hundred"
  else:
    return low_num_map[first_digit] + " hundred and " + two_digits(other_digits)

def num_to_word(x):
  if x < 10:
    return low_num_map[x]
  elif x < 100:
    return two_digits(x)
  elif x < 1000:
    return three_digits(x)
  elif x == 1000:
    return 'one thousand'

if __name__ == '__main__':

  sum = 0

  for i in range(1,1001):
    word = num_to_word(i)
    num_letters = len(word.replace(' ',''))
    sum = sum + num_letters

  print sum
