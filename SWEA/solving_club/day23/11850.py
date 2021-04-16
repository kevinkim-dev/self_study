#########################
#  SWEA number 11850
#  by 김승현                
#########################

# Q. 컨테이너 운반

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True) + [0]*M
    truck = sorted(list(map(int, input().split())), reverse=True)
    ci = 0
    total = 0
    for i in range(M):
        while truck[i] < container[ci]:
            ci += 1
        total += container[ci]
        ci += 1
    print("#%d %d" %(t, total))