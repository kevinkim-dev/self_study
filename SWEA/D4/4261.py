#########################
#  SWEA number 4261
#  by 김승현                
#########################

# Q. 빠른 휴대전화 키패드

def check_word(word):
    for i in range(len(word)):
        if word[i] not in key[int(S[i])]:
            return 0
    return 1

key = [0, 0, ('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z')]

for t in range(1, int(input())+1):
    S, N = input().split()
    N = int(N)
    word_list = list(input().split())
    ans = 0
    for word in word_list:
        if len(word) != len(S):
            continue
        ans += check_word(word)
    print("#%d %d" %(t, ans))
