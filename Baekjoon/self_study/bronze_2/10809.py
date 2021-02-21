###########################
#  BaekJoon 10809번
#  by 김승현                
###########################

# Q. 알파벳 찾기

al_idx = [-1]*26

word = input()
for i in range(len(word)):
    char = ord(word[i])-97
    if al_idx[char] == -1:
        al_idx[char] = i

print(*al_idx)