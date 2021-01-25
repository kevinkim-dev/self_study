# ##########################
#  project_euler number 18
#  by 김승현                
# ##########################

# Q. 삼각형을 따라 내려가면서 합이 최대가 되는 경로 찾기

import time

def go_left(tlist, height, index, tsum):
    return tsum + tlist[height+1][index]

def go_right(tlist, height, index, sum):
    return tsum + tlist[height+1][index+1]

# def binary(x):
#     binary_num = ''
#     while x > 0:
#         binary_num = binary_num + str(x % 2)
#         x = x // 2
#     return binary_num

start_time = time.time()

triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

triangle_list = triangle.split()
n = 1
while n*(n+1)/2 != len(triangle_list):
    n = n + 1
triangle_list = list(map(int, triangle_list))
triangle_2d_list = []
index = 0
for i in range(1, n+1):
    triangle_2d_list.append(triangle_list[index:index+i])
    index = index + i

tsum = triangle_2d_list[0][0]
max_sum = 0


for i in range(2 ** (n-1)):
    tsum = triangle_2d_list[0][0]
    index = 0
    root = f"%{n-1}s" % str(format(i, 'b')).zfill(n-1)
    for height in range(n-1):
        if tsum + 99*(n-1-height) < max_sum:
            break
        if root[height] == '0':
            tsum = go_left(triangle_2d_list, height, index, tsum)
        elif root[height] == '1':
            tsum = go_right(triangle_2d_list, height, index, tsum)
            index = index+1
    if tsum > max_sum:
        max_sum = tsum

end_time = time.time()

print(max_sum)
print(end_time - start_time)