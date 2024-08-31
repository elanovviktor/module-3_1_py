calls = 0
def count_calls(): # первая функция
    global calls
    calls += 1 # так называемый счетчик будщих функций.
def string_info(string) : # вторая функция, принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в
                     # верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(string), string.upper(), string.lower()) # lowwer и upper преоразует нижний регистр в вехний и наоборот.
def is_contains( string, list_to_search):# еще одна функция, здесь два параметра
    count_calls()
    for item in list_to_search: # ЗДЕСЬ перебираем каждый элемент в "list_...."
        if string.upper() == item.upper():# сравниваем string и текущий элемент в лист....
            return True # еслинайдено совпадение то труе
    return False # если нет совпадений то False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)# показывает колво вызовов функций
