def moouse():

    import random

    print('Добро пожаловать в игру Викторина')
    name = input('Как тебя зовут?:')

    print('Отлично!', name)
    answer = input('И так ты готов?:')


    FAMOUS_PEOPLE = {'Александр сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                 'Сергеевич Александрович Ессенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                 'Виктор Ребортович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                 'Сергей павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                 'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}


    rounds = int(input('Сколько раз вы хотите играть?:'))
    for i in range (rounds):
        name,date = random.choiсe(list(FAMOUS_PEOPLE.items()))
        answer = input (f'Когда родился {name}')
        if answer == date:
            print('Верно')
        else:
            print('Неверно')
    print('Пока')


print('Добро пожаловать в игру Викторина')
name = input('Как тебя зовут?:')

print('Отлично!',name)
answer = input('И так ты готов?:')


if answer == 'Да':
    moouse()
elif answer == 'Нет':
    print(('ну давай готовиться тогда'))
else:
    print('Не могу понять, что ты хочешь от меня)')