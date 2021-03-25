###########################
#  BaekJoon 5063번
#  by 김승현                
###########################

# Q. TGN

for t in range(int(input())):
    a, b, c = map(int, input().split())
    if b - c > a:
        print('advertise')
    elif b - c == a:
        print('does not matter')
    else:
        print('do not advertise')