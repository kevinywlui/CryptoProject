########## Cryptography Project #########
############### elliptic curve functions  ##############
## Kevin Lui -- Derek Hollowood ##



from fun import modinv

def ecmult(x,y,n,a,b,p):					#Multiplies the point (x,y) on the curve y^2 = x^3 + ax + b (over Z/pZ) by n

	if(n == 0):
		return (-1,0)					#(-1,0) is used to denote the point at infinity

	if (n % 2 == 0):
		return add(ecmult(x,y,n/2,a,b,p)[0],ecmult(x,y,n/2,a,b,p)[1],ecmult(x,y,n/2,a,b,p)[0],ecmult(x,y,n/2,a,b,p)[1],a,b,p)
	return add(x,y,ecmult(x,y,n-1,a,b,p)[0],ecmult(x,y,n-1,a,b,p)[1],a,b,p)


def add(x1,y1,x2,y2,a,b,p):					#adds the points (x1,y1) and (x2,y2) on the curve y^2 = x^3 + ax + b

  if(x1 == -1):
    return (x2, y2)					#case where first point is infinity
  if(x2 == -1):
    return (x1, y1)					#case where second point is infinity
  if(x1 == x2):
    if((y1 + y2) % p == 0):
      return (-1,0)					#case where points add to infinity
    l = ((((3*x1*x1)%p + a)%p)*modinv(2*y1,p)) % p
    x3 = ((l*l)%p - 2*x1) % p
    y3 = ((l*(x1 - x3))%p - y1) % p
    return (x3, y3)					#case where points are equal
  l = ((y2 - y1) * modinv(x2 - x1, p)) % p
  x3 = ((l*l)%p - x1 - x2) % p
  y3 = ((l*(x1 - x3))%p - y1) % p
  return(x3, y3)

