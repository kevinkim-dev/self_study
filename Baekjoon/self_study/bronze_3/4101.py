###########################
#  BaekJoon 4101번
#  by 김승현                
###########################

# Q. 크냐?

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print('YES') if a > b else print('NO')