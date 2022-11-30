numbers = list(range(100))#range возвращает лишь диапозон списка, а list формирует диапозон в список
print(numbers)

numbers2 = list(range(50, 100)) #при двух аргументах - 1й означает начало списка, 2ой-конец.
print(numbers2)

numbers3 = list(range(50, 101, 5)) #третий аргумент - шаг генерации
print(numbers3)

#далее обход списка - 1 способ, представленный в уроке
numbers4 = [1, 2, 3, 4, 5]

i = 0
length = len(numbers4) - 1

while i <= length:
    print(str(numbers4[i]) + "!")
    i+= 1

# далее обход списка - 2 способ, представленный в уроке

for element in numbers4:
    print(str(element) + "!!")

#выполнение кода указанное кол-во раз через range

for test in range(6):
    print("Hello")

#задача (какое число из индекса выведется?):
list = [1, 1, 2, 3, 5, 8, 13]
print( list[list[4]])
#8. Потому что