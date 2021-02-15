###########################
#  BaekJoon 10101번
#  by 김승현                
###########################

# Q. 삼각형 외우기

angle_list = [0]*3
for i in range(3):
    angle_list[i] = int(input())

for i in range(2, -1, -1):
    for j in range(i):
        if angle_list[j] > angle_list[j+1]:
            angle_list[j], angle_list[j+1] = angle_list[j+1], angle_list[j]

if angle_list[0] + angle_list[1] + angle_list[2] != 180:
    print('Error')
elif angle_list[0] == angle_list[1] == 60:
    print('Equilateral')
elif angle_list[0] == angle_list[1] or angle_list[1] == angle_list[2]:
    print('Isosceles')
else:
    print('Scalene')