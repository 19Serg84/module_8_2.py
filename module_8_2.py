def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Пытаемся добавить элемент к результату
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total, incorrect_data = personal_sum(numbers)

        # Вычисляем среднее арифметическое
        average = total / (len(numbers) - incorrect_data) if len(numbers) - incorrect_data > 0 else 0
        return average

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # коллекция с некорректными элементами
print(f'Результат 3: {calculate_average(567)}')  # не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # корректная коллекция