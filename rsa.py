########## Cryptography Project #########
############### RSA ##############
## Kevin Lui -- Derek Hollowood ##


from fractions import gcd
from random import randint
from time import time
from stest import stest
from collections import deque

def rsa(p,q,k):

  t = time()              # we start the clock here
  rngs = deque()          # store the rngs for testing

  n = p*q
  phi = (p-1) * (q-1)

  e = (p-1)               # this block of code choses e so that gcd(e,phi)=1
  while ( gcd(e,phi) != 1):
    e = randint(2, phi-1)
	
  x_0 = (p-1)             # this block of code choses x_0 so that gcd(x_0,phi)=1
  while ( gcd(e,phi) != 1):
    x_0 = randint(2, phi-1)


  z=0 

  for a in range(k):      # here we generate k values
    x_0 = pow(x_0,e,n)
    rngs.append(x_0%2)

  t=time()-t
  print('--------')
  print('{0} bits generated with RSA'.format(k))
  print('Generating time: {0}'.format(t))
  
  sarray = stest(rngs)
  sarray.insert(0,t)
  
  return sarray
