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

