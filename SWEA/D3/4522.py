#########################
#  SWEA number 4522
#  by 김승현                
#########################

# Q. 세상의 모든 팰린드롬

def is_pal(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i-1] and not (word[i] == '?' or word[-i-1] == '?'):
            return False
    return True

for t in range(1, int(input())+1):
    print("#%d Exist" %t) if is_pal(input()) else print("#%d Not exist" %t)