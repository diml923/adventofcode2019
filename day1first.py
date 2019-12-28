
f = open("input.txt", "r")
sum=0;
for x in f:
   sum = sum+ int(x)//3-2
print sum
