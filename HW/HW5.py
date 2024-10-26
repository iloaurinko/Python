# #Прямоугольник
#
# - Создайте класс Rectangle, который принимает ширину и высоту
# прямоугольника при создании и должен иметь соответствующие атрибуты
# width и height (целые числа).
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # - Создайте метод area(), который возвращает площадь прямоугольника.
    def area(self):
        return self.width * self.height

    # - Создайте метод perimeter(), который возвращает периметр
    # прямоугольника.
    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 10)
print(rect.width)  # Вывод: 5
print(rect.height)  # Вывод: 10
print(rect.area())  # Вывод: 50 (площадь)
print(rect.perimeter())  # Вывод: 30 (периметр)

# Пример:
rect = Rectangle(2, 4)
a = rect.area()  # Вернул 8
p = rect.perimeter()  # Вернул 12
print(a, p)


#
# 2 Автомобиль
#
# - Создайте класс Car, который принимает марку автомобиля (make) в виде
# строки и максимально возможную скорость (max_speed) в виде целого
# числа при создании. Также при инициализации (в теле __init__) экземпляра
# Car должен быть автоматически создан атрибут speed, равный 0 (текущая
# скорость автомобиля).
class Car:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    # - Создайте метод display_speed(), который выводит в консоль текущую
    # скорость автомобиля.
    def display_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч")
        return self.speed

    # - Создайте метод accelerate(), который увеличивает скорость автомобиля на
    # 10, при этом скорость автомобиля не должна превышать max_speed, если
    # вызывается accelerate() при максимальной скорости, то скорость не
    # должна увеличиваться.
    def accelerate(self):
        if self.speed + 10 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 10

    # - Создайте метод brake(), который уменьшает скорость автомобиля на 10,
    # при этом скорость автомобиля не может быть меньше 0. Если вызывается
    # метод brake() при скорости равной 0, то скорость не должна уменьшаться.
    def brake(self):
        if self.speed < 10:
            self.speed = self.speed
        else:
            self.speed -= 10


# Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()  # вывел в консоль 30


#
# 3
# Интернет-банк
#
# - Создайте класс BankAccount, который принимает имя владельца (name) в
# виде строки и текущее состояние счета (balance) в виде целого числа. Оба
# этих атрибута должны быть _защищенным.
class BankAccount:
    def __init__(self, name: str, balance: int):
        """     :param name: str — имя владельца счета.
                :param balance: int — текущее состояние счета.
                """
        self._name = name
        self._balance = balance

    # - Создайте метод deposit(), который принимает 1 аргумент (если не считать
    # self, конечно) amount (целое число). Метод должен увеличить текущий
    # баланс аккаунта на amount.
    def deposit(self, amount: int):
        """:param amount: int"""
        self._balance = self._balance + amount
        return self._balance

    # - Создайте метод withdraw(), который принимает 1 аргумент amount (целое
    # число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
    # денег на счету недостаточно, то метод выводит на экран “Недостаточно
    # средств!”.
    def withdraw(self, amount: int):
        """:param amount: int"""
        if (self._balance - amount) < 0:
            print("Недостаточно средств!")
        else:
            self._balance = self._balance - amount
            return self._balance

    # - Создайте метод get_balance(), который возвращает текущее значение
    # баланса аккаунта.
    def get_balance(self):
        return self._balance


# Пример:
account = BankAccount("Maria", 1000)
print(account.deposit(700))
print(account.withdraw(200))
print(account.get_balance())  # 1500
#
# 4
# Овердрафт
#
# - Создайте класс OverdraftAccount, унаследованный от вашего класса
# BankAccount из предыдущей задачи.
class OverdraftAccount(BankAccount):
# - Переопределите существующий метод withdraw(), но теперь, если баланс
# аккаунта меньше или равен 0, то это не выводит на экран сообщение
# “Недостаточно средств!”, а уменьшает баланс в минус.
    def withdraw(self, amount: int):
        self._balance = self._balance - amount
        return self._balance
# Пример:
jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance()) # -300
#
# Повторение прошлого материала.
#
# Ответьте на следующие вопросы:
# 1. Что такое and, or и not? Приведите пример их использования.
print(1 if 2 and 2 else 0)
print(True if 2 or 2 else 0)
print(1 != 0)
# 2. Что такое цикл? Чем отличается for от while?
for i in range(1, 10):
    print(i/2)
j = 1
while j <=10:
    print(j/2)
    j +=1
# 3. Как нельзя именовать переменную? Почему я не могу назвать переменную
# max или min?
# 4. Что такое функция? Зачем она нужна?
