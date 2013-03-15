########## Cryptography Project #########
############### Blum Blum Shub ##############
## Kevin Lui -- Derek Hollowood ##


from stest import stest
from fractions import gcd
from random import randint
from time import time
from sys import stdout
from collections import deque

def bbs(p,q,k):					#Blum Blum Shub Random Bit generator. Input two large primes 3mod4 and the number of bits in the output

  t = time()				      # start the clock
  rngs = deque()          # store the rngs for testing

  n = p*q
  phi = (p-1) * (q-1)			# phi is the number of elements in the multiplicative group of Z/nZ

  x_0 = (p-1)					    # x_0 is the seed
  while ( gcd(x_0,phi) != 1):					#this block of code chooses x_0 so that gcd(x_0,phi)=1
    x_0 = randint(2, phi-1)


  z=0					            # initialize z (the bit component)

  for a in range(k):      # generate sequence of k integers
    x_0 = (x_0*x_0) % n

    if (x_0 > n / 2):
      x_0 = n - x_0
    z = x_0 % 2
    rngs.append(z)



  t=time()-t
  print('--------')
  print('{0} bits generated with BBS'.format(k))
  print('Generating time: {0}'.format(t))
  
  sarray = stest(rngs)
  sarray.insert(0,t)
  
  return sarray
