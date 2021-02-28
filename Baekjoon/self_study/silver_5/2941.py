###########################
#  BaekJoon 2941번
#  by 김승현                
###########################

# Q. 크로아티아 알파벳

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()

for i in range(len(croatia)):
    if croatia[i] in string:
        string = string.replace(croatia[i], str(i))

print(len(string))



# used_letter = []
# string = input() + '  '
# idx = 0
# while idx < len(string):
#     if string[idx] == 'c':
#         if string[idx+1] == '=' or string[idx + 1] == '-':
#             used_letter.append(string[idx:idx+2])
#             idx += 2
#         else:
#             used_letter.append('c')
#             idx += 1
#     elif string[idx] == 'd':
#         if string[idx + 1] == '-':
#             used_letter.append(string[idx:idx+2])
#             idx += 2
#         elif string[idx + 1: idx + 3] == 'z=':
#             used_letter.append(string[idx:idx+3])
#             idx += 3
#         else:
#             used_letter.append('d')
#             idx += 1
#     elif string[idx] == 'z' or string[idx] == 's':
#         if string[idx+1] == '=':
#             used_letter.append(string[idx:idx+2])
#             idx += 2
#         else:
#             used_letter.append(string[idx])
#             idx += 1
#     elif string[idx] == 'l' or string[idx] == 'n':
#         if string[idx+1] == 'j':
#             used_letter.append(string[idx:idx+2])
#             idx += 2
#         else:
#             used_letter.append(string[idx])
#             idx += 1
#     else:
#         used_letter.append(string[idx])
#         idx += 1
# used_letter = list(set(used_letter))
# used_letter.remove(' ')
# print(len(used_letter))