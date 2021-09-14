###########################
#  BaekJoon 2193번
#  by 김승현                
###########################

# Q. 이친수

echin = []
e0, e1 = 0, 1
for i in range(int(input())):
    echin.append(e0)
    echin.append(e1)
    e0, e1 = e0 + e1, e0

print(echin[-1]+echin[-2])
