###########################
#  BaekJoon 10707번
#  by 김승현                
###########################

# Q. 수도요금

info_list = [0]*5
for i in range(5):
    info_list[i] = int(input())

x_cost = info_list[4] * info_list[0]

if info_list[4] > info_list[2]:
    y_cost = (info_list[4] - info_list[2])*info_list[3] + info_list[1]
else:
    y_cost = info_list[1]

if x_cost < y_cost:
    print(x_cost)
else:
    print(y_cost)