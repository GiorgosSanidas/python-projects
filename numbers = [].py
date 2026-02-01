numbers = []

for i in range(0,5):
    arithmos= int(input("Dwse arithmo:"))
    numbers.append(arithmos)

athrisma = numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]

print("to athrisma einai:", athrisma)

megaliteros = numbers[0]
mikroteros = numbers[0]

for i in range(0,5):
    if megaliteros < numbers[i]:
        megaliteros = numbers[i]
    
    if mikroteros > numbers[i]:
        mikroteros = numbers[i]

print("megaliteros arithmos: ", megaliteros)
print("mikroteros arithmos: ", mikroteros)

