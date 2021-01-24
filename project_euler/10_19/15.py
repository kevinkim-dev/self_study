###########################
#  project_euler number 15
#  by 김승현                
###########################

# def recursive_root(x, y):
#     if x == 0 and y == 0:
#         print("end")
#         return 1
#     elif x == 0 and y != 0:
#         print(f"{x},{y}")
#         return recursive_root(x, y-1)
#     elif x != 0 and y == 0:
#         print(f"{x},{y}")
#         return recursive_root(x-1, y)
#     else:
#         print(f"{x},{y}")
#         return recursive_root(x-1, y) + recursive_root(x, y-1)

# print(recursive_root(20, 20))
# crashed!!!

map = []

for i in range(21):
    map = map + [[0]*21]

map[0][0] = 1

for i in range(21):
    for j in range(21):
        if i == 0 and j == 0:
            map[i][j] = 1
        elif i == 0 and j != 0:
            map[i][j] = map[i][j-1]
        elif i != 0 and j == 0:
            map[i][j] = map[i-1][j]
        else:
            map[i][j] = map[i-1][j] + map[i][j-1]
        
print(map)
