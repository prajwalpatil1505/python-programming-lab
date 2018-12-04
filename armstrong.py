x=int(input())
s=0
z=x
while x>0:
  y=x%10
  s=y**3+s
  x=x//10
print(s)
if s==z:
  print("Armstrong number")
else:
  print("Not Armstrong number")
