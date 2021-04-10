#########################
#  SWEA number 10726
#  by 김승현                
#########################

# Q. 이진수 표현

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    bi = ''
    while M > 0:
        bi = str(M % 2) + bi
        M //= 2
    print("#%d ON" %t) if bi[-N:] == '1'*N else print("#%d OFF" %t)