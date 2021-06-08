#########################
#  SWEA number 4672
#  by 김승현                
#########################

# Q. 수진이의 팰린드롬

def is_pal(word):
    if word == word[::-1]:
        return True
    else:
        return False

for t in range(1, int(input())+1):
    word = ''.join(sorted(list(input())))
    l = len(word)
    ans = 0
    for i in range(1, l+1):
        for j in range(l+1 - i):
            if is_pal(word[j:j+i]):
                ans += 1
    print("#%d %d" %(t, ans))