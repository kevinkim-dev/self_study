###########################
#  BaekJoon 2702번
#  by 김승현                
###########################

# Q. 초6 수학

for _ in range(int(input())):
    a, b = map(int, input().split())
    a1, b1 = a, b
    while a1 != 0 and b1 != 0:
        if a1 > b1:
            a1 %= b1
        else:
            b1 %= a1
    gcd = a1 + b1
    print(a*b//gcd, gcd)
            