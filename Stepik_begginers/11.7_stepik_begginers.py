# объявление функции
def get_shipping_cost(quantity):
    sum = 0 
    if n == 1:
        return 1000
    else: sum =+ 1000
    for i in range(1, n):
        return 1000 + 120 * (quantity - 1)
#  return sum+ 120 * (quantity -1)

# считываем данные 
n = int(input()) 

print(get_shipping_cost(n))

from math import factorial as f
def compute_binom(n,k): return f(n)//(f(k)*f(n-k))
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))

num_ditc = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
# объявление функциb
def number_to_words(n):
    a=0
    b=0
    if n<=9: return num_ditc.get(n)
    if n > 9 and n % 10 == 0:
        return num_ditc.get(n)
    if n>10 and n%10 !=0:
        a= num_ditc.get(n-n%10)
        b= num_ditc.get(n%10)
        return f'{a} {b}'
        # считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
# объявление функции
lng_ru = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь',
          11:'ноябрь', 12:'декабрь'}

lng_en = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july', 8:'august', 9:'september', 10:'october',
          11:'november', 12:'december'}

def get_month(lan,n):
    if lan == "ru":
        return f'{lng_ru.get(n)}'
    if lan == 'en':
        return f'{lng_en.get(n)}'
# считываем данные
lan = input()
n = int(input())

# вызываем функцию
print(get_month(lan,n))

# объявление функции
def is_magic(date):
    d,m,g=map(int,date.split('.'))
    if d*m == g%100:
        return True
    else: return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def is_pangram(text):
    text = text.replace(" ","")
    text= text.lower()
    for i in abc:
        if i not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))