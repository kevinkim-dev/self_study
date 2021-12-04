###########################
#  BaekJoon 9610번
#  by 김승현                
###########################

# Q. 사분면

ans = [0]*5

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        ans[4] += 1
    elif x > 0:
        if y > 0:
            ans[0] += 1
        else:
            ans[3] += 1
    else:
        if y > 0:
            ans[1] += 1
        else:
            ans[2] += 1

for i in range(4):
    print(f'Q{i+1}: {ans[i]}')
print(f'AXIS: {ans[4]}')