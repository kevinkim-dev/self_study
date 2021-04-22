#########################
#  SWEA number 4698
#  by 김승현                
#########################

# Q. 테네스의 특별한 소수

prime_list = [i for i in range(1000001)]
for i in range(2, 1000001):
    if prime_list[i]:
        for j in range(i+i, 1000001, i):
            prime_list[j] = 0
prime_list[1] = 0

for t in range(1, int(input())+1):
    cnt = 0
    D, A, B = map(int, input().split())
    D = str(D)
    for i in range(A, B+1):
        if prime_list[i] and D in str(i):
            cnt += 1
    print("#%d %d" %(t, cnt))
