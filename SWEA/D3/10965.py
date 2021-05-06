#########################
#  SWEA number 10965
#  by 김승현                
#########################

# Q. 제곱수 만들기

prime_list = []
for i in range(2, int(10**(7/2))):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_list.append(i)

ans_list = []
for t in range(1, int(input())+1):
    a = int(input())
    ans = 1
    for i in prime_list:
        if a == 1:
            break
        cnt = 0
        while not a % i and a >= i:
            a //= i
            cnt += 1
        if cnt % 2:
            ans *= i
    ans *= a
    ans_list.append(ans)
for t, ans in enumerate(ans_list):
    print("#%d %d" %(t+1, ans))
        
