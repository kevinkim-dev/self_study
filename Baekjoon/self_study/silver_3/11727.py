###########################
#  BaekJoon 11727번
#  by 김승현                
###########################

# Q. 2xn 타일링 2

N = int(input())

tile = [1, 3]
while len(tile) < N:
    tile.append(tile[-1] + 2*tile[-2])

if N == 1:
    print(1)
else:
    print(tile[-1] % 10007)