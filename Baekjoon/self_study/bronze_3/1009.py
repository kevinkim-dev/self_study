###########################
#  BaekJoon 1009번
#  by 김승현                
###########################

# Q. 분산처리

left = [[10], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    a %= 10
    print(left[a][b % len(left[a])])