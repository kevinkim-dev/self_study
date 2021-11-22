###########################
#  BaekJoon 2563번
#  by 김승현                
###########################

# Q. 색종이

white = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            white[i][j] = 1

ans = 0

for i in range(100):
    for j in range(100):
        ans += white[i][j]

print(ans)