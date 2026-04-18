# **Описание**: Реализуйте функцию create_validator, которая принимает функцию-условие и возвращает новую функцию для проверки значений.
#
# **Входные данные**: Функция condition, которая принимает один аргумент и возвращает True или False
#
# **Выходные данные**: Функция-валидатор, которая принимает значение и возвращает True если условие выполнено, иначе False
#
# **Ограничения**: Функция должна работать с любыми условиями и типами данных
#
# **Примеры**:
# Input:
# def is_positive(x):
#     return x > 0
# validator = create_validator(is_positive)
# print(validator(5))
# Output: True
#
# Input:
# validator2 = create_validator(lambda x: len(x) > 3)
# print(validator2("hello"))
# Output: True
def is_positive(x):
    return x > 0
def create_validator(condition):
    validator = create_validator(is_positive)
    print(validator(5))
    