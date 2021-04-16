###########################
#  BaekJoon 1002번
#  by 김승현                
###########################

# Q. 터렛

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2)** 0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    if r1 + r2 < d:
        print(0)
    elif r1 + r2 == d:
        print(1)
    else:
        if max(r1, r2) - min(r1, r2) > d:
            print(0)
        elif max(r1, r2) - min(r1, r2) == d:
            print(1)
        else:
            print(2)
