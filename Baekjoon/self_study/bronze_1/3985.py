###########################
#  BaekJoon 3985번
#  by 김승현                
###########################

# Q. 롤 케이크

l, N = int(input()), int(input())

roll = [0]*l
want, get = [], []

for _ in range(N):
    s, e = map(int, input().split())
    want.append(e-s+1)
    tmp = 0
    for i in range(s, e+1):
        if roll[i-1]:
            continue
        roll[i-1] = 1
        tmp += 1
    get.append(tmp)

print(want.index(max(want))+1)
print(get.index(max(get))+1)
