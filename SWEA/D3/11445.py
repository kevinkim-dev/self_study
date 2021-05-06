#########################
#  SWEA number 11445
#  by 김승현                
#########################

# Q. 무한 사전

for t in range(1, int(input())+1):
    P, Q = input().strip(), input().strip()
    if Q == P + 'a':
        ans = 'N'
    else:
        ans = 'Y'
    print("#%d %s" %(t, ans))