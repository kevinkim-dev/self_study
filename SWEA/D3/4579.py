#########################
#  SWEA number 4579
#  by 김승현                
#########################

# Q. 세상의 모든 팰린드롬 2

def is_pal(word):
    while len(word) >= 2:
        if word[0] == '*' or word[-1] == '*':
            return True
        elif word[0] != word[-1]:
            return False
        word = word[1:-1]
    return True
    

for t in range(1, int(input())+1):
    word = input()
    print("#%d Exist" %t) if is_pal(word) else print("#%d Not exist" %t)