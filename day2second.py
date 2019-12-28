def recursivesum(x):
   sum=0
   if x <=0:
      return 0 #break out of loop
   else :
      return x+recursivesum(x//3-2)


f = open("input.txt", "r")
fuel=0;
for x in f:
   fuel += recursivesum(int(x)//3-2)
print fuel
