# my_list = [76, 92.3, "hello", True, 4, 76]
#
# my_list.append("apple")
# my_list.append(76)
#
# my_list.insert(3, "cat")
#
# my_list.insert(0, 99)
#
# # Find the index of "hello"
# hello_index = my_list.index("hello")
#
# count_76 = my_list.count(76)
#
# my_list.remove(76)
#
# my_list.pop(my_list.index(True))


# def sum_of_squares(number_list):
#     sum = 0
#     for number in number_list:
#         sum = sum  +number**2
#     return sum
#
# my_list = [4,5,6]
# print(sum_of_squares(my_list))

# def sum_evens(numbers_list):
#     sum = 0
#     for number in numbers_list:
#         if number % 2 == 0:
#             sum += number
#
#     return sum
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_list))

#
#
# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# my_list    = ("apple","cat", "lemon","snake","chips")
# print(count_five_letter(my_list))


#
# def sum_until_even(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             break
#         sum += number
#     return sum
#
#
# my_list = [1,  3,  5,  7, 8, 9 ]
# print(sum_until_even(my_list))

#
# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count = count + 1
#         if word == 'sam':
#             break
#     return count
#
# my_list = ("elma","armut","kamıl","sam","ben")
# print(count_until_sam(my_list))


#
# def replace(s,old,new):
#     places = s.split(old)
#     return new.join(places)
# def test(actual,expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# test(replace("Mississippi", "i" ,"I") , "MIssIssIppI")

#
# def max(numbers: list[int]) -> int:
#     largest = numbers[0]
#     for num in numbers[1:]:
#         if num > largest:
#             largest = num
#     return largest
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1000]
# print(max(my_list))