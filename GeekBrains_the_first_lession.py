a = 123
b = 1.23
c = "one-two-three"

print(a, "-", b, "-", c)
print("{} - {} - {}".format(a, b, c))
print(f"{a} - {b} - {c}")
print("{2} - {0} - {1}".format(a, b, c))

list = [1, 2, 3, 4, 5, "six", "seven", "eight", 9.0, 10.0, True, False] #bad_practice
print(list) #just_example
print(2 in list)

def another_func():
    """Document"""
    d = "local_var"
    e = input("Enter a number: ")
    print(d, e)
    print(another_func.__doc__)

another_func()

first_var = 48384938493
second_var = 555.5
third_var = round(first_var * second_var, 7)
print(third_var)

t = 5 > 4 > 3 > 2
print(t)
g = 10 > 5 or 5 > 1
print(g)

x = 200
y = 100
if x > y:
    print(x)
else:
    print(y)

for i in "qwerty":
    print(i)

help(y.bit_count)

z = "abcdefg"
print(z[2:5])