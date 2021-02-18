#########################
#  SWEA number 1926
#  by 김승현                
#########################

# Q. 간단한 369게임

n = int(input())
list369 = [0]*n
for i in range(1, n+1):
    num = i
    cnt = 0
    while num > 0:
        if (num % 10) % 3 == 0 and num % 10 != 0:
            cnt += 1
        num //= 10
    if cnt != 0:
        list369[i-1] = '-'*cnt
    else:
        list369[i-1] = str(i)
ans = " ".join(list369)
print(ans)