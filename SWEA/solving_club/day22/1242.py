#########################
#  SWEA number 1244
#  by 김승현                
#########################

# Q. 최대 상금

def change(num, m):
    global max_price
    if m == M:
        max_price = max(max_price, int(''.join(map(str, num))))
        return
    if num == max_num:
        if l == len(list(set(num))) and (M - m) % 2 == 1:
            num[-1], num[-2] = num[-2], num[-1]
        max_price = max(max_price, int(''.join(map(str, num))))
        return
    for i in range(l):
        if num[i] != max_num[i]:
            max_change = max(num[i+1:])
            for j in range(i+1, l):
                if num[j] == max_change:
                    num[i], num[j] = num[j], num[i]
                    change(num, m+1)
                    num[i], num[j] = num[j], num[i]
            break
    return


for t in range(1, int(input())+1):
    num, M = map(int, input().split())
    num = list(map(int, (str(num))))
    max_num = sorted(num, reverse=True)
    l = len(num)
    max_price = 0
    change(num, 0)
    print("#%d %d" %(t, max_price))