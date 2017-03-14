from random import randint
from math import sqrt, pi


def gcd(a, b):
  while b:
    a, b = b, a % b

  return a == 1


def calcPi(max_num=1000000, tries=100000000):
  i = 0
  coPrime = 0

  while i <= tries:
    a = randint(1, max_num)
    b = randint(1, max_num)

    if gcd(a, b):
      coPrime += 1

    i += 1

  x = (float(coPrime) / float(tries))
  piGuess = sqrt(6.0 / x)
  piDiff = abs(100 - ((piGuess / pi) * 100))

  print 'Your PI is:'
  print '       %.20f' % piGuess
  print '       A %.5f percent difference' % piDiff


if __name__ == '__main__':
  calcPi()
