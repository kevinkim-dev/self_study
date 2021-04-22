#########################
#  SWEA number 11907
#  by 김승현                
#########################

# Q. 이진 탐색

def binary_search(b):
    s, e = 0, N-1
    m = (s + e) // 2 
    flag = -1
    while s <= e:
        if A[m] > b:
            e, m = m - 1, (s + m - 1) // 2
            if flag == 0:
                return False
            else:
                flag = 0
        elif A[m] < b:
            s, m = m + 1, (m + 1 + e) // 2
            if flag == 1:
                return False
            else:
                flag = 1
        else:
            return True

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A, B = sorted(list(map(int, input().split()))), list(map(int, input().split()))
    cnt = 0
    for b in B:
        if b not in A:
            continue
        if binary_search(b):
            cnt += 1
    print("#%d %d" %(t, cnt))