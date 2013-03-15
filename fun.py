### useful functions

from math import sqrt

def modinv(a,p):					#for now, only works for p prime
  x=0
  y=1
  lastx=1
  lasty=0

  while(p != 0):
    quotient = int(a/p)
    c = p                         #c is a temp variable
    p = a % p
    a = c

    c = x
    x = lastx - quotient*x
    lastx = c

    c = y
    y = lasty - quotient*y
    lasty = c

  return lastx

def pfac(n):          # returns prime factorization in array for n=phi(prime)
  pf=[]
  
  i=2
  while(i <= sqrt(n)):
    
    if (n%i==0):
      pf.append(i)
    while(n%i==0):
      n=n/i
    
    i += 1
  pf.append(int(n))
  return pf
