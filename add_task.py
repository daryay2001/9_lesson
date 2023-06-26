# Написать игру "Угадай число" используя бинарный поиск:
# игрок загадывает число, пк отгадывает и показывает кол-во попыток.

def find_nums(first_num, last_num, number_to_find=0, count=0):
    while first_num <= last_num:
        middle_num = (first_num + last_num) // 2
        print(f"Is your number is {middle_num}?")
        user_choice = input("Enter + for yes and - for no: ")
        if user_choice == "+":
            count += 1
            number_to_find = middle_num
            print(f"Your number is {number_to_find}, {count} attempt")
            return
        elif user_choice == "-":
            count += 1
            print(f"Is your number is bigger than {middle_num}?")
            another_choice = input("Enter + for yes and - for no: ")
            if another_choice == "+":
                count += 1
                first_num = middle_num + 1

            elif another_choice == "-":
                count += 1
                last_num = middle_num - 1
            else:
                raise Exception("Please, enter + or -")
        else:
            raise Exception("Please, enter + or -")

    return -1

try:
    find_nums(1, 100)
except Exception as error:
    print(error)



# def binary_search(nums, search_item) -> int:
#     first_index = 0
#     last_index = len(nums) - 1
#
#     while first_index <= last_index:
#         middle_index = (first_index + last_index) // 2
#         if nums[middle_index] == search_item:
#             return middle_index
#         else:
#             if search_item < nums[middle_index]:
#                 last_index = middle_index - 1
#             else:
#                 first_index = middle_index + 1
#
#     return -1  # -1 означает что значение не найдено