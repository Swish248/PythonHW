#DheethyaB20182019Contest1DigitReassembly
#Contest 1
#Written by Dheethya Balaji from CompSciPrep. Grade 6

#1
number = input("Please input a number less than 10 to the power of 50: ")
x = len(number)
print(x)
#2
num = int(input("Please input a number less than 10 to the power of 50: "))
su = 0
while num > 0:
    d = num % 10
    num = num//10
    su += d
print(su)
#3
nu = input("Please input a number less than 10 to the power of 50: ")
i = 0
sum = 0
if len(nu) % 2 == 0:
    while i < len(nu) - 1:
        x = nu[i]
        sum = sum + int(x)
        i += 2
else:
    while i < len(nu):
        x = nu[i]
        sum = sum + int(x)
        i += 2


print(sum)

#4  i=i+2
n = input("Please input a number less than 10 to the power of 50: ")
y = n.count('4')
print(y)
#5
d = input("Please input a number less than 10 to the power of 50: ")
length = len(d)
if (length % 2) == 0:
    midpos = length // 2 - 1
    print(str(d[midpos]))
else:
    midpos = length // 2 + 1
    print(str(d[midpos - 1]))

#print("GITHUB IS STUPID AND SO AM I")