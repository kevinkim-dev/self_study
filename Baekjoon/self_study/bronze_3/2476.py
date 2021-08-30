###########################
#  BaekJoon 2476번
#  by 김승현                
###########################

# Q. 주사위 게임

max_prize = 0

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        prize = 10000 + a*1000
    elif a == b:
        prize = 1000 + a*100
    elif b == c:
        prize = 1000 + b*100
    elif c == a:
        prize = 1000 + a*100
    else:
        prize = max(a, b, c)*100
    max_prize = max(max_prize, prize)

print(max_prize)