########## Cryptography Project #########
############### Elliptic Curves ##############
## Kevin Lui -- Derek Hollowood ##


from time import time
from stest import stest
from ecur import ecmult
from random import randint
from sys import stdout
from collections import deque

def dec(p,k):					#Dual Elliptic Curve Deterministic Random Bit Generator with k bits generated by the curve y^2 = x^3 + ax + b over Z/pZ where p is a prime 3mod4
  
  rngs = deque()
  t = time()				        	# start the clock
  n = 2	              				# number seed is multiplied by at each step
  

  a=0
  b=0
  while(4*pow(a,3)+27*pow(b,2)==0): #here we ensure the curve is nonsingular
    a=randint(1,p-1)
    b=randint(1,p-1)

  c=0					                # used to produce seed

  while(c!=1):                # (x,y) is the seed
    x = randint(0,p-1)
    c = pow(x^3 + a*x + b, int((p-1)/2), p)


  y = pow(x^3 + a*x + b, int((p+1)/4), p)

  z=0					                # initialize z (the bit component)
  

  for a in range(k):					# generate sequence of k points
    (x,y) = ecmult(x,y,n,a,b,p)
    z = (x + y) % 2
    rngs.append(z)
		
  t=time()-t
  print('--------')
  print('{0} bits generated with Dual E. Curve'.format(k))
  print('Generating time: {0}'.format(t))
  
  sarray = stest(rngs)
  sarray.insert(0,t)
  
  return sarray
