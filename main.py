# Алгоритм быстрой сортировки.
# Написать функцию, которая реализует алгоритм "Быстрой сортировки".
# Вводятся следующие параметры:
# - количество значений (с использованием конструкции try-except)
# - ввод чисел с клавиатуры (в список) (с использованием конструкции try-except)
#
# + Сортировка "пузырьком"
# quicksor

def bubble(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
try:
    lista = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите количество элементов: ")))]
    print(bubble(lista))
except ValueError:
    print("Некорректный ввод")








