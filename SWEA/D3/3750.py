#########################
#  SWEA number 3750
#  by 김승현                
#########################

# Q. Digit sum

ans_list = []
T = int(input())
for t in range(1, T+1):
    N = int(input())
    while N >= 10:
        new_N = 0
        while N != 0:
            new_N += N % 10
            N //= 10
        N = new_N
    ans_list.append(N)
for i in range(T):
    print("#%d %d" %(i+1, ans_list[i]))