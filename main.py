"""
    Это исполнитель языка fantasy v.0

    << - оператор добавления всех элементов массива справа в левый контейнер.
    , - оператор дополнения элемента, который после, к массиву спереди
"""

from plugin import Variables  # импорт типа переменные

variables = Variables()  # создаем массив переменных

exit()

# This is Variables sample Python script.

echo = []  # массив, выводим на екран каждый раз для тестирования редактируя

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows,
#  actions, and settings.


from others import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# text = ""


text = copy("script.fan")

# parser:
arr = text.split()  # делим строку на массив слов
# TODO: нужно поменять концепцию, теперь нужно рассматривать и переходы на новую
#  строку чтобы удалять комментарии - хотя я не вижу разумного применения в
#  языке, пока что

# run:
i, j = 0, 0
tmp = []
ignore = False

while i < len(arr):
    if arr[i] == ",":
        tmp += [arr[i - 1], arr[i + 1]]
        del echo[i - 1]
        ignore = True  # нужно проигнорировать следующее слово.
    elif ignore:
        echo.append(tmp)  # добавляем на вывод наш образовавшийся массив
        ignore = False  # указываем что следующее слово уже не часть массива
        tmp = []  # обнуляем массив, так как его мы уже отдали на вывод
    else:  # нужно что-то вроде: elif arr[i + 1] != ",":
        echo.append(arr[i])  # нужно не добавлять как то элемент который только
        #  образуется как массив
    i += 1

# test:
print(text)
print(tmp)
print(echo)
print(arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
