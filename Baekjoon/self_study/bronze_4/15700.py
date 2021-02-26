###########################
#  BaekJoon 15700번
#  by 김승현                
###########################

# Q. 타일 채우기 4

n, m = map(int, input().split())

tile = (n//2)*m
if n % 2 == 1:
    tile += m//2

print(tile)