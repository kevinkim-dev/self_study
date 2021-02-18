#########################
#  SWEA number 11552
#  by 김승현                
#########################

for t in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    max_count = 0
    for chr in str1:
        cnt = str2.count(chr)
        if cnt > max_count:
            max_count = cnt
    print("#%d %d" %(t, max_count))