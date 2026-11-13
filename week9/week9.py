# def is_odd(n):
#     return n % 2 == 1
#
# print(is_odd(13))
#
# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(is_leapyear(2000))


# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#         print(i ,total)
#
# print(print_triangular_numbers(100))

#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2 , n):
#         if n % i == 0:
#             return False
#         return True
#
# print(is_prime(10))


#
# def reverse(s)
#     result = ""
#     for char in s:
#         result = char + result
#     return result
# print(reverse("hello"))
#
#
# def reverse_slice(s):
#     return s[::-1]
#
# print(reverse_slice("kamil"))


# def remove_all_occurences(sub , s):
#     return s.replace(sub , "")
#
# print(remove_all_occurences("h", "hello"))





# def substitute(message,key):
#     alphabet = "abcçdefgğhıijklmnoöpqrsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index != -1:
#             result = ch  + result
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtgdjeopwmaolqhtyuvzmacydişl"
# print(substitute("hello guys", key))
# #
# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if ch.lower() not in result.lower():
#             result= result + ch
#     return result
#
#
# print(remove_dups("hello world"))



