import random

def bubble_sort(nums):

    not_sorted = True

    while not_sorted:
        not_sorted = False
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                not_sorted = True

# my_nums = [1, 5, 2, 3, 4, 6]

# bubble_sort(my_nums)
# print(my_nums)

def selection_sort(nums):
    for i in range(len(nums)):
        min_value_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_value_index]:
                min_value_index = j

        nums[i], nums[min_value_index] = nums[min_value_index], nums[i]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        insert_item = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > insert_item:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = insert_item


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle_index = len(nums) // 2

    left_list = merge_sort(nums[:middle_index])
    right_list = merge_sort(nums[middle_index:])

    return merge(left_list, right_list)

def partition(nums, low_index, high_index):
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
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):

    def helper_sort(items, low_index, high_index):
        if low_index < high_index:
            split_index = partition(items, low_index, high_index)
            helper_sort(items, low_index, split_index)
            helper_sort(items, split_index + 1, high_index)

    helper_sort(nums, 0, len(nums)-1)


#
my_nums = []

for i in range (10):
    my_nums.append(random.randint(-10, 10))
# #
print(my_nums)
# # # selection_sort(my_nums)
# # insertion_sort(my_nums)
# merge_sort(my_nums)
# another_list = merge_sort(my_nums)
# print(another_list)
quick_sort(my_nums)
print(my_nums)



