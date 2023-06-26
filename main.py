import random


def generate_random_list(list_len, start_value=1, end_value=100):
    nums = []
    for i in range(list_len):
        nums.append(random.randint(start_value, end_value))

    return nums

#######
# Сортировка пузырьком (Bubble sort)
#
# При каждом проходе алгоритма по внутреннему циклу очередной наибольший элемент массива ставится
# на своё место в конце массива рядом с предыдущим «наибольшим элементом»,
# а наименьший элемент перемещается на одну позицию к началу массива («всплывает» до нужной позиции)

def bubble_sort(nums):
    not_sorted = True

    while not_sorted:
        not_sorted = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                not_sorted = True

####
# Сортировка выбором - это алгоритм сортировки массива или списка путем постепенных перестановок
# наименьших элементов в начало списка или наибольших в конец.

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
#Сортировка вставками (англ. Insertion sort) — алгоритм сортировки, в котором элементы входной
# последовательности просматриваются по одному, и каждый новый поступивший элемент размещается
# в подходящее место среди ранее упорядоченных элементов
def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # сохраняем ссылку на индекс предыдущего значения
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # вставка элемента
        nums[j + 1] = item_to_insert
#
# Принцип Разделяй и властвуй
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # сравниваем первые элементы в начале каждого списка
            # если первый элемент левого подсписка меньше - добавляем его
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                # иначе добавим из правого подсписка
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # если достигнут конец левого списка - элементы правого списка добавим в конец sorted_list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

#
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle_index = len(nums) // 2

    left_list = merge_sort(nums[:middle_index])
    right_list = merge_sort(nums[middle_index:])

    return merge(left_list, right_list)
#
#
def partition(nums, low_index, high_index):
    # выбираем средний элемент в качестве опорного
    # так же возможен выбор первого, последнего или произвольного эл-тов в качестве опорного
    pivot = nums[(low_index + high_index) // 2]
    i = low_index - 1
    j = high_index + 1

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше чем элемент с индексом j (справа от опорного) -
        # то меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

# Быстрая сортировка, сортировка Хоара.
# Один из самых быстрых известных универсальных алгоритмов сортировки массивов.
def quick_sort(nums):
    # вспомогательная функция
    def _quick_sort(items, low_index, high_index):
        if low_index < high_index:
            split_index = partition(items, low_index, high_index)
            _quick_sort(items, low_index, split_index)
            _quick_sort(items, split_index + 1, high_index)

    _quick_sort(nums, 0, len(nums) - 1)

#
# #
def linear_search_from_start(nums, search_item) -> int:
    for i in range(len(nums)):
        if nums[i] == search_item:
            return i
    return -1


def linear_search_from_end(nums, search_item) -> int:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == search_item:
            return i
    return -1
#
#
# # бинарный поиск работает ТОЛЬКО на отсортированном массиве
def binary_search(nums, search_item) -> int:
    first_index = 0
    last_index = len(nums) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if nums[middle_index] == search_item:
            return middle_index
        else:
            if search_item < nums[middle_index]:
                last_index = middle_index - 1
            else:
                first_index = middle_index + 1

    return -1  # -1 означает что значение не найдено

#
# my_list = generate_random_list(5)
# print(my_list)
# # bubble_sort(my_list)
# # selection_sort(my_list)
# # insertion_sort(my_list)
# # my_list = merge_sort(my_list)
# quick_sort(my_list)
# print(my_list)
# #
numbers = [1, 4, 10, 5, 2, 10, 4, 10, 3]
numbers.sort()
print(numbers)
value = 5
# result = linear_search_from_start(numbers, value)
# result = linear_search_from_end(numbers, value)
result = binary_search(numbers, value)
# print(result)
#
if result != -1:
    print(f"{value} found on index: {result}")
else:
    print(f"{value} not found!")
