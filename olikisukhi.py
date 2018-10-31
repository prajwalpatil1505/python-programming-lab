x=int(input())
if x<0:
  print("Factorial value does not exist")
elif x==1 or x==0:
  print("Factorial value is 1")
else:
  f=1
  while x>1:
    f=f*x
    x=x-1
print(f)
