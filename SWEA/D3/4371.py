#########################
#  SWEA number 4371
#  by 김승현                
#########################

# Q. 항구에 들어오는 배

for t in range(1, int(input())+1):
    N = int(input())
    happyday = list(int(input())-1 for _ in range(N))[1:]
    happyday_bool = [1] * (N-1)
    for i in range(N-1):
        if happyday_bool[i]:
            for j in range(i+1, N-1):
                if happyday[j] % happyday[i] == 0:
                    happyday_bool[j] = 0
    print("#%d %d" %(t, happyday_bool.count(1)))

