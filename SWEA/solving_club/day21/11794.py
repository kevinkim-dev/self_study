#########################
#  SWEA number 11794
#  by 김승현                
#########################

# Q. 이진수2

for t in range(1, int(input())+1):
    num = float(input())
    bi_num = ''
    for i in range(-1, -13, -1):
        if not num:
            break
        bi_num += str(int(num // 2**i))
        num %= 2**i 
    print("#%d overflow" %t) if num else print("#%d %s" %(t, bi_num))
        
        # print(2**i, num // 2**i, int(num // 2**i), str(int(num // 2**i)))
    