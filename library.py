import sys
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


