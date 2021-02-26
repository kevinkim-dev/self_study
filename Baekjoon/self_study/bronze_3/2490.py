###########################
#  BaekJoon 2490번
#  by 김승현                
###########################

# Q. 윷놀이

check = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    print(check[list(map(int, input().split())).count(0)])