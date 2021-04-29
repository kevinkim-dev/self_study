#########################
#  SWEA number 2948
#  by 김승현                
#########################

# Q. 문자열 교집합

for t in range(1, int(input())+1):
    N, M = map(int, input().split())    a_list, b_list = list(input().split()), list(input().split())
    A, B = [set() for _ in range(51)], [set() for _ in range(51)]
    for a in a_list:
        A[len(a)].add(a)
    for b in b_list:
        B[len(b)].add(b)
    cnt = 0
    for i in range(1, 51):
        for x in A[i]:
            if x in B[i]:
                cnt += 1
    print("#%d %d" %(t, cnt))
