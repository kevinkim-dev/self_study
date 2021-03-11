###########################
#  BaekJoon 1547번
#  by 김승현                
###########################

# Q. 공

now = 1

for t in range(int(input())):
    a, b = map(int, input().split())
    if a == now:
        now = b
    elif b == now:
        now = a

print(now) 