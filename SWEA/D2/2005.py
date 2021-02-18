#########################
#  SWEA number 2005
#  by 김승현                
#########################

# Q. 파스칼의 삼각형

# for t in range(1, int(input())+1):
#     print("#%d" %t)
#     size = int(input())
#     array = [0]*size
#     for i in range(size):
#         array[i] = [0]*(i+1)
#         for j in range(i+1):
#             if j == 0 or j == i:
#                 array[i][j] = 1
#             else:
#                 array[i][j] = array[i-1][j-1] + array[i-1][j]
#         print(*array[i])

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_list = []
    for i in range(1, N + 1):
        num_list += [[0] * i]

    num_list[0][0] += 1
    num_list[1][0] += 1
    num_list[1][1] += 1
    # print(num_list)

    for i in range(2, N):
        num_list[i][0] += 1
        num_list[i][i] += 1
        for j in range(1, i):
            num_list[i][j] = num_list[i - 1][j] + num_list[i - 1][j - 1]

    print('#%d' %t)
    for num in num_list:
        print(num)