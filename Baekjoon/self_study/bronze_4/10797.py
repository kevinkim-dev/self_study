###########################
#  BaekJoon 10797번
#  by 김승현                
###########################

# Q. 10부제

no_num = int(input())

num_list = list(map(int, input().split()))
count = 0

for num in num_list:
    if num == no_num:
        count += 1

print(count)