i = 1
while 1 == 1:
    print("Hi " + str(i))
    i += 1

    if i == 100:
        break

print("After break")

number = 0

while number <= 100:
    number += 1
    if (number % 2) != 0:
        continue;
    print("Even number " + str(number))