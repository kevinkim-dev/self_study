###########################
#  BaekJoon 10818번
#  by 김승현                
###########################

# Q. 최소, 최대

n = int(input())

n_list = sorted(list(map(int, input().split())))
print(n_list[0], n_list[n-1])
