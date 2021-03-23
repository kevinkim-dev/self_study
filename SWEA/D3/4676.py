#########################
#  SWEA number 4676
#  by 김승현                
#########################

# Q. 늘어지는 소리 만들기

for t in range(1, int(input())+1):
    string = list(input())
    H = int(input())
    loc = sorted(list(map(int, input().split())))
    for h in range(H):
        string.insert(loc[h]+h, '-')
    print("#%d %s" % (t, ''.join(string)))