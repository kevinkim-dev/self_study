###########################
#  BaekJoon 15953번
#  by 김승현                
###########################

# Q. 상금 헌터

a_price = [5000000, 3000000, 2000000, 500000, 300000, 100000]
b_price = [5120000, 2560000, 1280000, 640000, 320000]

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    total = 0
    ai = 0
    if a:
        for i in range(1, 7):
            ai += i
            if a <= ai:
                total += a_price[i-1]
                break
    if b:
        for i in range(1, 6):
            if b <= 2**i - 1:
                total += b_price[i-1]
                break
    print(total)