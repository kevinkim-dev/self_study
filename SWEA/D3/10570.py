#########################
#  SWEA number 10570
#  by 김승현                
#########################

# Q. 제곱 팰린드롬 수

def palindrom(x):
    x = str(x)
    return x == x[::-1]

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    if a**(1/2) == int(a**(1/2)):
        A = int(a**(1/2))
    else:
        A = int(a**(1/2))+1
    if b**(1/2) == int(b**(1/2)):
        B = int(b**(1/2))
    else:
        B = int(b**(1/2))
    cnt = 0
    for num in range(A, B+1):
        if palindrom(num) and palindrom(num**2):
            cnt += 1
    print("#%d %d" %(t, cnt))