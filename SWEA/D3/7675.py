#########################
#  SWEA number 7675
#  by 김승현                
#########################

# Q. 통역사 성경이

def find_name(word):
    if 65 <= ord(word[0]) <= 90:
        for i in range(1, len(word)):
            if not 97 <= ord(word[i]) <= 122:
                return False
        return True
    else:
        return False

for t in range(1, int(input())+1):
    N = int(input())
    names = [0]*N
    words = list(input().split())
    idx = 0
    for word in words:
        if word[-1] in ('.', '!', '?'):
            if find_name(word[:-1]):
                names[idx] += 1
            idx += 1
        else:
            if find_name(word):
                names[idx] += 1
    ans = ' '.join(list(map(str, names)))
    print("#%d %s" %(t, ans))