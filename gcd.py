def extended_gcd(a,b):
  a_, b_ = a, b
  x0,x1,y0,y1 = 1, 0, 0, 1
  print("q\tr\tx\ty\ta\tb\tx2\tx1\ty2\ty1")
  print(f"-\t-\t-\t-\t{a}\t{b}\t{x0}\t{x1}\t{y0}\t{y1}")
  while b:
    q = a // b
    r = a - q*b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
    a, b = b, r
    print(f"{q}\t{r}\t{x1}\t{y1}\t{a}\t{b}\t{x0}\t{x1}\t{y0}\t{y1}")

  print(" \t \t \t \t¯\t \t¯\t \t¯ \t")
  print(f"a•x + b•y = d")
  print(f"{x0}•{a_} + {y0}•{b_} = НОД({a_},{b_}) = {a}")
  print("\nd  x  y")
  return a, x0, y0