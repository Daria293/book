import sys
class LibraryErrors(Exception):
    "Базовый класс ошибок библиотеки"
class TextFilterEmpty(LibraryErrors):
    "не передан текст фильтра"
class InputError(LibraryErrors):
    "передана кривая команда"
class ParameterSortedError(LibraryErrors):
    "Неправильный параметр сортировки"
books = {"Ущелье дьявола": "А. Дюма", "Королева Марго": "А. Дюма", "Том Сойер": "Марк Твен", "Белый вождь": "Майн Рид", "Граф Монте Кристо": "А. Дюма"}

def all_books(books):
    print("Название".ljust(30), "Автор")
    print("*" * 40)
    for book, author in books.items():
        print(book.ljust(20), "|".ljust(10), author)

list_books =  []
for key in books.keys():
    list_books.append(key)

list_author = set()
for value in books.values():
    list_author.add(value)

print(list_books)
print(list_author)

action = sys.argv[1]
arg = sys.argv[2]
pred = lambda item: item[1] == arg
mapper = lambda item: f"{item[0]} — {item[1]}"
n = list(map(mapper, books.items()))
items = list(books.items())
filtered = filter(pred, items) 
result = list(map(mapper, filtered))
sorted_items = sorted(items, key=lambda it: it[1].lower())
l = list(map(mapper, sorted_items))

if action == "filter":
    filtered = filter(lambda item: item[1] == arg, items)
    result = list(map(lambda item: f"{item[0]} — {item[1]}", filtered))
    for line in result:
        print(line)
elif action == "sort":
    if arg == "author":
        sorted_items = sorted(items, key=lambda it: it[1].lower())
    elif arg == "book":
        sorted_items = sorted(items, key=lambda it: it[0].lower())
    else:
        print('Для sort используйте arg: "author" или "book"')
        sys.exit(1)
    result = list(map(lambda item: f"{item[0]} — {item[1]}", sorted_items))
    for line in result:
        print(line)

else:
    print('Использование: python library.py <action> <arg> action: filter|sort arg: для filter — имя автора; для sort — "author" или "book"')

def main():
    try:
        # Проверка аргументов
        if len(sys.argv) < 2:
            raise InputError("Не передан action")
        action = sys.argv[1]

        # Пример: для filter требуется второй аргумент
        if action == 'filter':
            if len(sys.argv) < 3:
                raise TextFilterEmpty('не передан текст фильтра')
            # Ваша логика фильтрации тут

        elif action == 'sort':
            if len(sys.argv) < 3:
                raise ParameterSortedError('Неправильный параметр сортировки')
            # Ваша логика сортировки тут

        else:
            raise InputError(f'Неизвестный action: {action}')

    except TextFilterEmpty as e:
        print('Ошибка фильтра:', e)
        return
    except ParameterSortedError as e:
        print('Ошибка параметра сортировки:', e)
        return
    except InputError as e:
        print('Ошибка ввода:', e)
        return
    except Exception as e:
        # Общий обработчик неожиданных ошибок — полезен при отладке
        print('Непредвиденная ошибка:', e)
        return            

