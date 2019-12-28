

with open("input2.txt", "r") as f:


# f.read reads one single character at a time, while split will return a splited list

  for x in f :
    number = x.split(",")
 # change numbers
 # run program

  # python's for is foreach loop, there's no direct counter
  # BUT! you can use, array and it's array methods to manipulate the list

number = [int(string) for string in number]
number[1]=12
number[2]=2

#print(number)
#print(len(number))
x = len(number)
i=0
while i<range(x) :
    #print(i)
    if number[i] == 1 :
        a = number[i+3]
        b = number[i+1]
        c = number[i+2]
        number[a] = number[b]+number[c]
        i +=4
        print(i)
        #print("when number is 1")
    elif number[i] == 2 :
       a = number[i+3]
       #print(a)
       b = number[i+1]
       c = number[i+2]
       #print(number[a])
       #print(number[b])
       #print(number[c])
       number[a] = (number[b])*(number[c])
       i +=4
    elif number[i] == 99 :
        break
    else :
       i+=1
       print("Unexpected input!")




print(number)

# consider the case when 1, 2 is used as noneopcode
