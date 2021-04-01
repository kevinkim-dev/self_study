#########################
#  SWEA number 3233
#  by 김승현                
#########################

# Q. 정삼각형 분할 놀이

for t in range(1, int(input())+1):
    A, B = map(int, input().split())
    ans = 0
    for n in range(A//B):
        ans += n*2+1
    print("#%d %d" %(t, ans))