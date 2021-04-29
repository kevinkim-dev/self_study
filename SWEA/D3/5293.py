#########################
#  SWEA number 5293
#  by 김승현                
#########################

# Q. 이진 문자열 복원
# 00, 01, 10, 11

for t in range(1, int(input())+1):
    A, B, C, D = map(int, input().split())
    ans = 'impossible'
    total = A + B + C + D
    if total == 1:
        ans = '00'*A + '01'*B + '10'*C + '11'*D
    elif B-C == 1:
        ans = '0'*A + '01'*B + '1'*D
    elif C-B == 1:
        ans = '1'*D + '10'*C + '0'*A
    elif B == C and B != 0:
        ans = '0'*(A+1) + '1'*(D+1) + '01'*(B-1) + '0'
    elif B == C and B == 0 and not(A and D):
        if A:
            ans = '0'*(A+1)
        elif D:
            ans = '1'*(D+1)
    print("#%d %s" %(t, ans))