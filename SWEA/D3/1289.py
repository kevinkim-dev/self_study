#########################
#  SWEA number 1289
#  by 김승현                
#########################

# Q. 원재의 메모리 복구하기

for t in range(1, int(input())+1):
    string = input()
    bit = '0'
    cnt = 0
    for char in string:
        if bit != char:
            bit = char
            cnt += 1
    print("#%d %d" %(t, cnt))