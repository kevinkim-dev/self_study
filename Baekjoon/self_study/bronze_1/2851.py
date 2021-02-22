###########################
#  BaekJoon 2851번
#  by 김승현                
###########################

# Q. 슈퍼 마리오

mush_list = [int(input()) for i in range(10)]

eat = [0]
flag = 0
for i in range(10):
    eat.append(eat[i] + mush_list[i])
    if eat[i+1] >= 100:
        print(eat[i+1]) if abs(100-eat[i]) >= abs(100-eat[i+1]) else print(eat[i])
        flag = 1
        break
if flag == 0:
    print(eat[-1])