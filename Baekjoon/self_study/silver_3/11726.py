###########################
#  BaekJoon 11726번
#  by 김승현                
###########################

# Q. 2xn 타일링

N = int(input())

tile = [1, 2]
while len(tile) < N:
    tile.append(tile[-1] + tile[-2])
print(tile[-1] % 10007)