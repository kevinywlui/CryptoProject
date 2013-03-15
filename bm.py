########## Cryptography Project #########
############## Blum-Micali  ##############
## Kevin Lui -- Derek Hollowood ##


from time import time
from stest import stest
from collections import deque
from fun import pfac
from random import randint

def bm(p,k):


  t=time()					#start the clock
  rngs=deque()


  #find primitive root mod p and set to g
  phi=p-1
  pf=pfac(phi)    # pf is the array of prime factors of phi

  works = 0					#find a primitive root modp
  while works == 0:
    works = 1
    g=randint(2,p-2)
    for j in pf:
      if pow(g,int(phi/j),p)==1:
        works=0
        break

  x_0 = randint(2,p-1)					#x_0 is the seed

  
  for a in range(k):					#generate a sequence of k integers
    x_0=pow(g,x_0,p)
    if x_0 < float(p-1)/2:
      z=1					#z is the actual bit
    else:
      z=0
    rngs.append(z)
  
  
  t=time()-t
  print('--------')
  print('{0} bits generated with BM'.format(k))
  print('Generating time: {0}'.format(t))
  
  sarray = stest(rngs)
  sarray.insert(0,t)
  
  return sarray
