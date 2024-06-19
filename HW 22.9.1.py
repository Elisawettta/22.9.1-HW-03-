array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
element = float(input("Введите любое число: "))

def sort_func (array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] >= element and array[middle - 1] < element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(sort_func(array), " - массив отсортирован")
left = float(array[0])
right = float(array[-1])
if element < left or element > right:
    print("Число не входит в заданный диапазон")
else:
    print("Номер позиции меньшего числа", binary_search(array, element, 0, len(array) - 1))

