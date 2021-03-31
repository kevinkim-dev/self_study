###########################
#  BaekJoon 1920번
#  by 김승현                
###########################

# Q. 수 찾기

N = int(input())
a_set = set(list(map(int, input().split())))
M = int(input())
x_list = list(map(int, input().split()))
for x in x_list:
    print(int(x in a_set))