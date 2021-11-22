###########################
#  BaekJoon 10103번
#  by 김승현                
###########################

# Q. 주사위 게임

a, b = 100, 100

for i in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        b -= x
    elif x < y:
        a -= y

print(a)
print(b)