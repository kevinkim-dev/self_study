#########################
#  SWEA number 3376
#  by 김승현                
#########################

# Q. 파도반 수열

padoban = [1, 1, 1]

for t in range(1, int(input())+1):
    N = int(input())
    while len(padoban) < N:
        padoban.append(padoban[-2] + padoban[-3])
    print("#%d %d" %(t, padoban[N-1]))