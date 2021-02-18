#########################
#  SWEA number 3143
#  by 김승현                
#########################

# b의 길이가 체크되는 곳까지 체크한다
# 있으면 b의 길이만큼 idx 추가, cnt += 1
# 없으면 idx += 1, cnt += 1
# A의 마지막이 B면 pass
# 아니었다면 전체길이 - idx로 남은 길이를 cnt에 추가

for t in range(1, int(input())+1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    idx = 0
    cnt = 0
    while idx < a-b+1:
        if A[idx:idx+b] == B:
            idx += b
        else:
            idx += 1
        cnt += 1
    if A[-b:] == B and idx == b:
        pass
    else:
        cnt += a-idx

    print("#%d %d" %(t, cnt))