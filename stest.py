##### Tester function ######
#
#
# This implements the frequency test, bit switch test and the poker test


from math import floor
from time import time
def stest(rngs):

  size = len(rngs)                # here rngs should be a deque type
  t=time() 

  freq = 0                        # here we count the number of 1s
  switch = 0                      # here we count the number of bit switches
  
  # poker test
  poker = [0]*32          # each entry correspond to the binary representation
                          # for example, poker[2] count the number of bit sequences
                          # of the form 00010
  
  switchtemp=0                    # temp variable for switch


  numof5sequence=floor(size/5)
  for k in range(numof5sequence):  # we consider disjoint 5 bit sequences
    


    index=0             # this will tell us what kind of bit sequence this is

    for i in range(5):            # we consider disjoint 5 bit sequences
      z = rngs.popleft()
      freq += z                   # here we count 1s
      switch += z^switchtemp       # here we count switches-"^" is xor
      switchtemp=z
      
      index += pow(2,4-i)*z         # here we convert the 5 bit sequence into
                                    # the index for the poker array
    poker[index] += 1               
                                    
      
  

# here we compute chi square of poker test
  chi2 = 0
  expected = float(numof5sequence)/32
  j=0
  for i in poker:
    chi2 += pow(i-expected,2)/expected
# we test multiples of 5 bits so we set tsize to that
  tsize=(size//5)*5
  
  print('Frequency of 1s: {0}'.format(float(freq)/tsize))
  print('Frequency of switches: {0}'.format(float(switch)/tsize))
  print('Chi Square of Poker test: {0}'.format(chi2))

  return [float(freq)/tsize,float(switch)/tsize,chi2]
