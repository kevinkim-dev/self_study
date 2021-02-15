###########################
#  BaekJoon 2480번
#  by 김승현                
###########################

# Q. 주사위 세개

num_list = list(map(int, input().split()))

for i in range(2, -1, -1):
    for j in range(i):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

if num_list[0] == num_list[1] == num_list[2]:
    money = 10000 + num_list[0]*1000
elif num_list[0] == num_list[1] or num_list[1] == num_list[2]:
    money = 1000 + num_list[1] * 100
else:
    money = num_list[2] * 100

print(money)    