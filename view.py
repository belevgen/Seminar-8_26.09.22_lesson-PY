def menu():
    print("Приветствуем Вас в нашей справочной системе")
    print('''Меню:
    1 Добавить контакт
    2 Удалить контакт 
    3 Посмотреть контакты
    4 Найти контакт
    5 Импорт контакта
    6 Экспорт контакта
    7 Выход из справочника
      ''')


menu()


def control_menu():
    while True:
        number = input('Выберите нужное действие: ')
        if number.isdigit():
            number = int(number)
            if number > 0 and number <= 7:
                return number
            else:
                print('Введите правильный выбор в меню')
                continue
        print('Вы ввели не цифру! Начните сначала!')
        continue


print(control_menu())
