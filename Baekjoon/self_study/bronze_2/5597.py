###########################
#  BaekJoon 5597번
#  by 김승현                
###########################

# Q. 과제 안 내신 분..?

students = [0]*30

for _ in range(28):
    students[int(input())-1] = 1

for i in range(30):
    if students[i]:
        continue
    print(i+1)