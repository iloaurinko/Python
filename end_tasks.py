# # import random
# #
# # numbers = list(range(2, 10, 2)) + [3]
# #
# # num = random.choice(numbers)
# # print(num)
# import random
#
# numbers = [1, 2, 4, 6, 7, 9]
#
# rand_numbers = random.sample(numbers, 3)
# print(rand_numbers)

# def sum(x,y):
#     return x+y
# def minus(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return "Can't divide by zero"

# import random
# n = random.randint(1,100)
# print('Добро пожаловать в числовую угадайку')
#
# def is_valid(s):
#     return 1 <= int(s) <= 100
#
# while True:
#     number = input('Your number between 1 and 100 is: ', )
#     if is_valid(number) == False:
#         print('А может быть все-таки введем целое число от 1 до 100?')
#         continue
#     else:
#         number=int(number)
#         break
# def compare_num(s):
#     if number < n:
#         return print("Ваше число меньше загаданного, попробуйте еще разок")
#     elif number> n: return print('Ваше число больше загаданного, попробуйте еще разок')
#     elif number == n: return print('Вы угадали, поздравляем!')
# print(n)
# attempts = 0
#
# if n != number:
#     number = int(input("Введите число: "))
#     is_valid(number)
#     compare_num(number)
#     attempts +=1
#
# print(f'Число попыток {attempts}')
#
# def continue_game(): # Предложение продолжить игру
#     ans = input('Хотите продолжить ("д"/"н")?\n')
#     while True:
#         if ans not in ('y', 'д', 'n', 'н'):
#             ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
#         elif ans in ('n', 'н'):
#             print('До новых встреч!!!')
#             return False
#         else:
#             return True
# continue_game()
#
# def game(): # Запуск игры
#     print('Добро пожаловать в числовую угадайку!')
#     while True:
#         print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
#         x, y = int(input()), int(input())
#         if x > y:
#             x, y = y, x
#         print('Введите число от', x, 'до', y, '\n')
#         compare_num(x, y)
#         if continue_game():
#             continue
#         else:
#             break

# from random import *
#
# # алгоритм игры
# def guessing_game(x, y):
#     phrases_too_much = ['Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
#                         'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
#     phrases_too_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
#                         'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!']
#     phrases_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
#                       'Горячо!']
#     phrases_guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
#     phrases_too_soon = ['Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число', 'Скажи честно, ты подглядывал?',
#                         'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']
#     if x > y:
#         x, y = y, x
#         num_0 = randint(x, y)
#         print('Я загадал число от', x, 'до', y, 'Попробуй угадать!')
#     else:
#         num_0 = randint(x, y)
#         print('Я загадал число от', x, 'до', y, 'Попробуй угадать!')
#     count = 0
#     while True:
#         num_1 = int(input())
#         count += 1
#         if num_1 == num_0:
#             if count == 1:
#                 print('Скажи честно, ты подглядывал?')
#                 if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#                     start()
#                 else:
#                     print('Приходи, когда появится желание сыграть снова :)')
#                     break
#             elif 1 <= count <= 5:
#                 print(choice(phrases_too_soon))
#                 if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#                     start()
#                 else:
#                     print('Приходи, когда появится желание сыграть снова :)')
#                     break
#             else:
#                 print(choice(phrases_guessed))
#                 if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#                     start()
#                 else:
#                     print('Приходи, когда появится желание сыграть снова :)')
#                     break
#         elif num_1 > num_0:
#             if abs(num_1 - num_0) < 5:
#                 print(choice(phrases_too_much), choice(phrases_almost), sep='\n')
#             else:
#                 print(choice(phrases_too_much))
#         elif num_1 < num_0:
#             if abs(num_1 - num_0) < 5:
#                 print(choice(phrases_too_little), choice(phrases_almost),  sep='\n')
#             else:
#                 print(choice(phrases_too_little))
#
# # описание правил
# def game_rules():
#     print('Отлично! Давай ознакомлю тебя с правилами игры.')
#     print('Я загадаю число, а ты будешь его отгадывать.')
#     print('Диапазон чисел ты выберешь сам.')
#     print('К примеру, если ты укажешь диапазон чисел от 0 до 100, я не смогу загадать число "101" :)')
#     print('Я попрошу тебя ввести границы диапазона. Границы не должны совпадать! Так играть мы не сможем.')
#     input('А теперь напиши что-нибудь, чтобы я был уверен, что ты понял правила игры :)')
#
# # проверка правильности
# def is_valid_x(x):
#     if x.isdigit() is False:
#         print('Ты ввел не число :(')
#         print('Что ж, ладно, введи новые числа.')
#         start()
#
# def is_valid_xy(x, y):
#     while x == y:
#         print('Ты ввел одинаковые числа. Я же говорил, что так играть мы не сможем :(')
#         print('Что ж, ладно, введи новое число.')
#         start()
#     if y.isdigit() is False:
#         print('Я запутался :( Это не число')
#         print('Давай заново :)')
#         start()
#     else:
#         return True
#
# # запуск игры
# def start():
#     x = input('Введи первую границу диапазона: ')
#     is_valid_x(x)
#     y = input('Введи вторую границу диапазона: ')
#     if is_valid_xy(x, y) is True:
#         x, y = int(x), int(y)
#         guessing_game(x, y)
#
# # приглашение в игру
# if input('Не желаешь сыграть в игру? Введи "да" или "нет" ').lower() in ['да', 'lf']:
#     game_rules()
#     start()
# else:
#     if input('Это не займёт много времени и сил. Если всё таки надумал, введи "да" :)').lower() in ['да', 'lf']:
#         game_rules()
#         start()
#     else:
#         print('Приходи, когда появится желание сыграть :)')

#Магический шар
# from random import choice
# import emoji
# if __name__ == '__main__':
#     list_answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Опеределенно да',
#                     'Можешь быть уверен да', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы',
#                     'Знаки говорят да', 'Да','Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
#                     'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет',
#                     'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
#     request = ['Задавай вопрос', 'Пиши вопрос и я дам на него ответ', 'Отлично. Теперь можешь задавать свой вопрос',
#                'Задавай свой тупой вопрос']
#     print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
#     print('А вас как зовут?')
#     user_name = input()
#     print(f'Привет {user_name}')
#     while True:
#         ball_answer = choice(list_answers)
#         ball_request = choice(request)
#         print(ball_request, user_name)
#         user_ans = input()
#         print(ball_answer, user_name)
#         print('Ко мне вопросы остались?')
#         user_last_quest = input()
#         if user_last_quest.lower() == 'нет' or user_last_quest.lower() == 'no':
#             print(emoji.emojize('Пока. Обращайся, если что :thumbs_up:'))
#             break

#Passwords
import random

d = int(input('Количество паролей для генерации: '))
len_parol = int(input('Длину паролей: '))
digit = '23456789' if input('Включать ли цифры: ').lower() == 'да' else ''
big = 'ABCDEFGHIJKMNPQRSTUVWXYZ' if input('Включать ли прописные буквы: ').lower() == 'да' else ''
small = 'abcdefghjklmnpqrstuvwxyz' if input('Включать ли строчные буквы? ').lower() == 'да' else ''
symvols = '!#$%&*+-=?@^_' if input('Включать ли символы !#$%&*+-=?@^_? ').lower() == 'да' else ''
neformal = 'il1Lo0O' if input('Исключать ли неоднозначные символы il1Lo0O? ').lower() == 'да' else ''
chars = digit + big + small + symvols + neformal

for _ in range(d):
    for _ in range(len_parol):
        print(random.choice(chars), end='')
    print()

# ОТВЕТ  Лхкрпч, фьш мпъэпь, ьпщхш пцэ чк ымпьп!
# Код для решения
# Запускаем цикл for, который будет перебирать каждый символ в введенной строке (input() возвращает строку).
for i in input():
    # Проверяем, является ли символ буквой.
    if i.isalpha():
        # С помощью ord(i) получаем числовое значение символа i в кодировке Unicode.
        # Затем к этому числу добавляем 10 (смещение на 10 позиций).
        # Важно: ord('я') - последний символ в русской алфавитной таблице, и это значение используется
        # для определения "грани" алфавита, чтобы учесть круговое смещение (после 'я' идет опять 'а').
        # Затем мы берем остаток от деления на ord('я'), чтобы убедиться, что остаемся в пределах алфавита.
        # Далее мы используем chr() для преобразования числового значения обратно в символ и выводим его.
        print(chr((ord(i) + 10) % ord('я')), end='')
    else:
        # Если символ не является буквой, мы просто выводим его без изменений.
        print(i, end='')
#"To be, or not to be, that is the question!"
# ОТВЕТ  Kf sv, fi efk kf sv, kyrk zj kyv hlvjkzfe!
# Код для решения
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Определяем базу для сдвига в зависимости от регистра буквы (A для больших, a для маленьких)
            base = ord('A') if char.isupper() else ord('a')
            # Применяем сдвиг и учитываем, что алфавит круглый (после 'Z' идет 'A', после 'z' идет 'a')
            shifted_char = chr(((ord(char) - base + shift) % 26) + base)
            result += shifted_char
        else:
            # Если символ не является буквой, оставляем его неизменным
            result += char
    return result
text_to_encrypt = "To be, or not to be, that is the question!"
shift_amount = 17
encrypted_text = caesar_cipher(text_to_encrypt, shift_amount)
print("Зашифрованный текст:", encrypted_text)

# ОТВЕТ  Скупой теряет все, желая все достать.
# Код для решения
# Исходный зашифрованный текст
s = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
# Пустая строка для расшифрованного текста
m = ''
# Проходим по каждому символу в зашифрованном тексте
for i in s:
    if i.isalpha():           # Проверяем, является ли символ буквой
        m += chr(ord(i) - 7)  # Расшифровываем символ с учетом сдвига влево на 7 позиций
    else:
        m += i                # Если символ не буква, оставляем его неизменным
# Приводим результат к нижнему регистру
m = m.lower()
# Первую букву текста делаем заглавной
print(m.capitalize())

