###########################
#  BaekJoon 9085번
#  by 김승현                
###########################

# Q. 더하기

T = int(input())
for _ in range(T):
    N, num_list = int(input()), list(map(int, input().split()))
    print(sum(num_list))