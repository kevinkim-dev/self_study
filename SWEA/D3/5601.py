#########################
#  SWEA number 5601
#  by 김승현                
#########################

# Q. 쥬스 나누기

for t in range(1, int(input())+1):
    n = input()
    juice = [('1/' + n)]*int(n)
    print("#%d" %t, end=' ')
    print(*juice)