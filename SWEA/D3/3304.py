#########################
#  SWEA number 3304
#  by 김승현                
#########################

# Q. 최장 공통 부분 수열

# 시간초과
def dp(ai, bi):
    if ai == 0 or bi == 0:
        return 0
    elif a[ai-1] == b[bi-1]:
        return dp(ai-1, bi-1) + 1
    else:
        return max(dp(ai-1, bi), dp(ai, bi-1))


for t in range(1, int(input())+1):
    a, b = input().split()
    al, bl = len(a), len(b)
    D = [[0]*(bl+1) for _ in range(al+1)]
    print("#%d %d" %(t, dp(al, bl)))


# def LCS(ai, bi, l):
#     global max_length
#     if ai >= al or bi >= bl:
#         max_length = max(l, max_length)
#         return
#     LCS(ai + 1, bi, l)
#     x = -1
#     for i in range(bi, bl):
#         if a[ai] == b[i]:
#             x = i
#             break
#     if x != -1:
#         LCS(ai+1, x+1, l+1)
#     return


# def LCS():
#     max_length = 0
#     while q:
#         ai, bi, l = q.pop(0)
#         if min(al-ai, bl-bi) < max_length - l:
#             continue
#         if ai >= al or bi >= bl:
#             max_length = max(max_length, l)
#         q.append((ai+1, bi, l))
#         for i in range(bi, bl):
#             if a[ai] == b[i]:
#                 q.append((ai+1, i+1, l+1))
#                 break
#             max_length = max(max_length, l)
#     return max_length