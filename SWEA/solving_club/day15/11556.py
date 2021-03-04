#########################
#  SWEA number 11556
#  by 김승현                
#########################

# Q. 부분집합의 합

# 해당수를 넣을지 말지 선택 후 q에 넣는다
# i를 올리고 넣을지 말지 선택후 q에 넣는다... 반복
# 길이가 3이면 합이 맞는지 보고 리턴, 아니면 반복 

def subset(k):
    N = len(q)
    for i in range(N):
        tmp = q[i]
        if len(tmp) == n and sum(tmp) == ans-k:
            return 1
        elif len(tmp) < n+1:
            q.append(tmp+[k])
    return subset(k+1) if k < 12 else 0

for t in range(1, int(input())+1):
    n, ans = map(int, input().split())
    q = [[0]]
    print("#%d %d" %(t, subset(1)))

# def subset(k):
#     N = len(q)
#     for _ in range(N):
#         tmp = q.pop(0)
#         q.append(tmp)
#         if len(tmp) == n and sum(tmp) == ans-k:
#             return 1
#         elif len(tmp) < n+1:
#             q.append(tmp+[k])
#     return subset(k+1) if k < 12 else 0

# for t in range(1, int(input())+1):
#     n, ans = map(int, input().split())
#     q = [[0]]
#     print("#%d %d" %(t, subset(1)))