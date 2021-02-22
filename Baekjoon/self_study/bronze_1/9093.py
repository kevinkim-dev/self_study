###########################
#  BaekJoon 9093번
#  by 김승현                
###########################

# Q. 단어 뒤집기

for t in range(int(input())):
    words = input().split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    print(*words)
