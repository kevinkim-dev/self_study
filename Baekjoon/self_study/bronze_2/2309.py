###########################
#  BaekJoon 2309번
#  by 김승현                
###########################

# Q. 일곱 난쟁이

from itertools import combinations

nine = []
for _ in range(9):
    nine.append(int(input()))
for comb in combinations(list(range(9)), 7):
    height = 0
    seven = []
    for com in comb:
        seven.append(nine[com])
        height += nine[com]
    if height == 100:
        break
seven.sort()
for i in range(7): 
    print(seven[i])