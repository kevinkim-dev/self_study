###########################
#  BaekJoon 14470번
#  by 김승현                
###########################

# Q. 전자레인지

num_list = [0]*5
for i in range(5):
    num_list[i] = int(input())

if num_list[0] < 0:
    ice_time = -(num_list[0] * num_list[2]) + num_list[3]
    melt_time = num_list[1]*num_list[4]
else:
    ice_time = 0
    melt_time = (num_list[1]-num_list[0]) * num_list[4]

print(ice_time + melt_time)