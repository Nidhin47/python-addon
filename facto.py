def facto(n):
  fact=1
  x=range(1,n+1)
  for i in x:
   fact=fact*i
  return(fact)

def sumf(a,b):
 y=facto(a)
 print "factorial of number1 is",y
 z=facto(b)
 print "factorial of number2 is",z
 print "sum of factorials is:",y+z

sumf(input("enter number1:"),input("enter number2:"))

