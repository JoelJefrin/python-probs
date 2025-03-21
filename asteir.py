num= [5,2,5,2,2,]
for i in num:
    output=''
    for count in range (i):
        output +='X'

    print(output)

numbers= [2,5,7,3,9,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max= number
print(max)
