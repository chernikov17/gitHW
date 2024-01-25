def extended_gcd(a,b):
  x0,x1,y0,y1 = 1, 0, 0, 1

  while b:
    q = a // b
    r = a - q*b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
    a, b = b, r

  return a, x0, y0