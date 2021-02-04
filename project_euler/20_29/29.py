# ##########################
#  project_euler number 29
#  by 김승현                
# ##########################

# Q. 2 ≤ a ≤ 100 이고 2 ≤ b ≤ 100인 a, b로 만들 수 있는 ab의 개수

expo_list = []

for i in range(2, 101):
    for j in range(2, 101):
        expo = i ** j
        if expo_list.count(expo) == 0:
            expo_list.append(expo)
    
print(len(expo_list))