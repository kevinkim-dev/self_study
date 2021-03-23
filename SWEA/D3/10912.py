#########################
#  SWEA number 10912
#  by 김승현                
#########################

# Q. 외로운 문자

for t in range(1, int(input())+1):
    string = list(input())
    ans = ''
    for n in range(97, 123):
        if string.count(chr(n)) % 2:
            ans += chr(n)
    print("#%d %s" %(t, ans if ans else 'Good'))
