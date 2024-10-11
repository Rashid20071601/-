def calculate_structure_sum(structure):
    sum_ = 0
    # Прописываем условие при помощи цикла 1 для списка, кортежа, множества
    if isinstance(structure, (list, tuple, set)):
        for item in structure:
            sum_ += calculate_structure_sum(item)

    # иначе добавляем к sum_ ключ(key) и значение(value)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)

    # иначе добавляем к sum_ - int и float
    elif isinstance(structure, (int, float)):
        sum_ += structure

    # иначе добавляем k sum_ длину строки
    elif isinstance(structure, str):
        sum_ += len(structure)

    # Возвращаем значение sum_
    return sum_


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)