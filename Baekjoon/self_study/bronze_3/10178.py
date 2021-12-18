###########################
#  BaekJoon 10178번
#  by 김승현                
###########################

# Q. 할로윈의 사탕

for _ in range(int(input())):
    c, v = map(int, input().split())
    get, left = c // v, c % v
    print(f'You get {get} piece(s) and your dad gets {left} piece(s).')