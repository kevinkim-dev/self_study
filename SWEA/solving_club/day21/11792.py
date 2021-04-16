#########################
#  SWEA number 11792
#  by 김승현                
#########################

# Q. 이진수

for t in range(1, int(input())+1):
    N, hexa_num = input().split()
    bi_num = ''
    for n in range(int(N)):
        bi_num += bin(int(hexa_num[n], 16))[2:].zfill(4)
    print("#%d %s" %(t, bi_num))