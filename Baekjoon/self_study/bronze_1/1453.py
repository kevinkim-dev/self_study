###########################
#  BaekJoon 1453번
#  by 김승현                
###########################

# Q. 피시방 알바

t = int(input())
num_list = list(map(int, input().split()))
new_list = list(set(num_list))
print(len(num_list)- len(new_list))