def print_spam(number):
    print("spam")
    print("spam")
    print(number)

print_spam(2)

def multiply(number):
    print(number * 2)

multiply(3)

def max(x, y):
    if x > y:
        return x
    else:
        return y
    print("NEVER") #это не выведется на экран, поскольку ретерн останавливает исполнение программы

x = input("Enter a number 1: ")
y = input("Enter a number 2: ")

print (max(x, y))

