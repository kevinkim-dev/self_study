###########################
#  BaekJoon 1037번
#  by 김승현                
###########################

# Q. 약수

N = int(input())
num_list = sorted(list(map(int, input().split())))

print(num_list[0]*num_list[-1])