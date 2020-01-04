import copy 

with open("input2.txt", "r") as f:
    
    for a in f:
        number = a.split(",")
        og_number = [int(string) for string in number]
	
        for x, y in ((a, b) for a in range(100) for b in range(100)):
            number = og_number
            number[1] = x
            number[2] = y
            i = 0
            z = len(number)
            while i < z:
                if number[i] == 1:
                    a = number[i + 3]
                    b = number[i + 1]
                    c = number[i + 2]
                    number[a] = number[b] + number[c]
                    i += 4
                elif number[i] == 2:
                    a = number[i + 3]
                    b = number[i + 1]
                    c = number[i + 2]
                    number[a] = (number[b]) * (number[c])
                    i += 4
                elif number[i] == 99:
                    break
            if number[0] == 19690720:
                print("found it", 100*x+y)

                break

print(number)


