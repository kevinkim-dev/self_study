###########################
#  BaekJoon 1931번
#  by 김승현                
###########################

# Q. 회의실 배정

con_list = []


for _ in range(int(input())):
    s, e = map(int, input().split())
    con_list.append([s, e])

con_list.sort(key=lambda x: (x[1], x[0]))

ans, now = 0, 0

for s, e in con_list:
    if s >= now:
        ans += 1
        now = e

print(ans)