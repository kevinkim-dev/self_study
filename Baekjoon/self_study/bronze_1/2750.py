###########################
#  BaekJoon 2750번
#  by 김승현                
###########################

# Q. 수 정렬하기

num = int(input())

num_list = [0]*num

for i in range(num):
    num_list[i] = int(input())

for i in range(num-1, 0, -1):
    for j in range(0, i):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for i in range(num):
    print(num_list[i])