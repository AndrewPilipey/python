test = [1, 2, 3, [4, 5, 6]]
print(test[3][1])
print("Len of the list equals: " + str(len(test)))

test1 = ['a', 'b', 'c']
print(test1 * 2, test1 + ['d', 'e', 'f'])

test2 = "Hello"
print(test2[2])

test3 = ["Alex Smith", "Andrew Phillips", "Edvard Nor"]
if "Andrew Phillips" in test3:
    print("Andrew Phillips is in the list. We found him.")
if "Elina Terner" not in test3:
    print("Elina Terner is not in the list. We didn't found her")

test4 = []
test4.append("Hello ") #добавление в список
test4.append("my")
test4.append(" collegue")
print(test4, str(len(test4)))
test4.remove("Hello ") #удаление из списка
print(test4)

test5 = [5, 3, 2, 5, 6, 7, 3]
test5.insert(0, 9) #ставка элемента списка в указанное место
print(test5, "Max number in the list te st5 equals:", max(test5), "Min number in the list test5 equals:", min(test5))
print(test5.count(3)) #метод подсчета указанного значения элементов

test6 = [1, 2, 3, 4]
test6.reverse() #метод используется вне вывода print
print(test6)