
from rsa import rsa
from bm import bm
from bbs import bbs
from dec import dec
from random import randint


# found on "http://www.bigprimes.net/archive/prime/14000000/"
primes=[32416190071,32416190039,32416189919,32416189867,32416189859,32416189511,32416189499,32416189459,32416189391,32416189291,32416189231,32416189163,32416189079,32416189063,32416189031,32416189019,32416188899,32416188887,32416188859,32416188839]


def main():

  size=pow(10,6)          # number of bits generated for each run

  rsastest=[0]*4
  bmstest=[0]*4
  bbsstest=[0]*4
  decstest=[0]*4

  for i in range(10):
    for j in range(10):
      
      temp=rsa(primes[2*i],primes[2*i+1],size)
      for k in range(4):
        rsastest[k]+=temp[k]

      temp=bm(primes[i],size)
      for k in range(4):
        bmstest[k]+=temp[k]

      temp=bbs(primes[2*i],primes[2*i+1],size)
      for k in range(4):
        bbsstest[k]+=temp[k]

      temp=dec(primes[i],size)
      for k in range(4):
        decstest[k]+=temp[k]

  
  rsastest=[a/100 for a in rsastest]
  bmstest=[a/100 for a in bmstest]
  bbsstest=[a/100 for a in bbsstest]
  decstest=[a/100 for a in decstest]

  print('---------')
  print('Testing Done')
  print('---------')
  print('Result of RSA Bit Generator:')
  print('Average generating time: {0}'.format(rsastest[0]))
  print('Frequency of 1s: {0}'.format(rsastest[1]))
  print('Frequency of switches: {0}'.format(rsastest[2]))
  print('Chi Square of Poker test: {0}'.format(rsastest[3]))
  print('---------')
  print('Result of Blum-Micali Generator:')
  print('Average generating time: {0}'.format(bmstest[0]))
  print('Frequency of 1s: {0}'.format(bmstest[1]))
  print('Frequency of switches: {0}'.format(bmstest[2]))
  print('Chi Square of Poker test: {0}'.format(bmstest[3]))
  print('---------')
  print('Result of Blum Blum Shub:')
  print('Average generating time: {0}'.format(bbsstest[0]))
  print('Frequency of 1s: {0}'.format(bbsstest[1]))
  print('Frequency of switches: {0}'.format(bbsstest[2]))
  print('Chi Square of Poker test: {0}'.format(bbsstest[3]))
  print('---------')
  print('Result of Dual Elliptic Curve Bit Generator:')
  print('Average generating time: {0}'.format(decstest[0]))
  print('Frequency of 1s: {0}'.format(decstest[1]))
  print('Frequency of switches: {0}'.format(decstest[2]))
  print('Chi Square of Poker test: {0}'.format(decstest[3]))


if __name__ == "__main__":
    main()
