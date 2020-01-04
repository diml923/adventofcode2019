

with open("input2.txt", "r") as f:


  for x in f :
    number = x.split(",")
    number = [int(string) for string in number]
    number[1]=12
    number[2]=2
    x = len(number)
    i=0

while i<range(x) :
 
    if number[i] == 1 :
        a = number[i+3]
        b = number[i+1]
        c = number[i+2]
        number[a] = number[b]+number[c]
        i +=4
               
    elif number[i] == 2 :
       a = number[i+3]
       b = number[i+1]
       c = number[i+2]
      
       number[a] = (number[b])*(number[c])
       i +=4
    elif number[i] == 99 :
        break
    else :
       i+=1
       print("Unexpected input!")



print(number)

