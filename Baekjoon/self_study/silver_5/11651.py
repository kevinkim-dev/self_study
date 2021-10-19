###########################
#  BaekJoon 11651번
#  by 김승현                
###########################

# Q. 좌표 정렬하기2

dots = dict()

for _ in range(int(input())):
    x, y = map(int, input().split())
    if dots.get(y):
        dots[y].append([x, y])
    else:
        dots[y] = [[x, y]]

for ky in sorted(dots.keys()):
    a = dots[ky]
    a.sort(key=lambda x: x[0])
    for x, y in a:
        print(f'{x} {y}')