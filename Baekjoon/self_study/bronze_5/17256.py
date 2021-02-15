###########################
#  BaekJoon 17256번
#  by 김승현                
###########################

# Q. 달달함이 넘쳐 흘러

a_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

print(c_list[0] - a_list[2], int(c_list[1] / a_list[1]), c_list[2] - a_list[0])