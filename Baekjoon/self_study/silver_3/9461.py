###########################
#  BaekJoon 9461번
#  by 김승현                
###########################

# Q. 파도반 수열

padoban = [1, 1, 1]

for _ in range(int(input())):
    N = int(input())
    while len(padoban) < N:
        padoban.append(padoban[-2] + padoban[-3])
    print(padoban[N-1])