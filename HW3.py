# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
for i in range(3):
    print(my_list[i])
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
sumlist=0
for i in range(7):
    if type(list_1[i]) == int:
        sumlist += list_1[i]
    elif "a" in list_1[i]:
        print(list_1[i])
print(sumlist)
# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
list2= ['cat', 'dog', 'horse', 'cow']
print(tuple(list2))
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family_1 = list(input("Введите состав семьи1: ").split())
family_2 = list(input("Введите состав семьи2: ").split())
if len(family_1)> len(family_2):
    print("Семья 1 больше")
elif len(family_1) == len(family_2):
    print('Equal')
else: print("Семья 2 больше")

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan.
# В значения можете передать информацию о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
film = {'title': "To be the best",
'director': "Jonh Jonson", 'year': "2024", 'budget':"100 000", 'main_actor': "Jonh Travolta", 'slogan': "Be the best"}
print(film.keys())
print(film.values())
print(film.items())
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
sumval = 0
for i in my_dictionary.values():
   sumval += i
print(sumval)
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
list_2 = [1, 2, 3, 4, 5, 3, 2, 1]
list_3 = list(set(list_2))
print(list_3)
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
s_intersection = set1 & set2
print(s_intersection)
s_sym_dif = set1 ^ set2
# s_sym_dif = s_1.symmetric_difference(s_2)
print(s_sym_dif)
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))