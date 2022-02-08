###########################
#  BaekJoon 9081번
#  by 김승현                
###########################

# Q. 단어 맞추기

# import sys

# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = list(input())
    for i in range(len(word)-1, 0, -1):
        if word[i] <= word[i-1]:
            continue
        min_dif, min_idx = 27, -1
        for j in range(i, len(word)):
            if word[j] > word[i-1] and ord(word[j]) - ord(word[i-1]) < min_dif:
                min_dif = ord(word[j]) - ord(word[i-1])
                min_idx = j
        if min_idx == -1:
            break
        word[i-1], word[min_idx] = word[min_idx], word[i-1]
        word[i:] = sorted(word[i:])
        break
    print(''.join(word))