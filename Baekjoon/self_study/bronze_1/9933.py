###########################
#  BaekJoon 9933번
#  by 김승현                
###########################

# Q. 민균이의 비밀번호

word_list = []

for _ in range(int(input())):
    word_list.append(input())

for word in word_list:
    if word[::-1] in word_list:
        print(len(word), word[(len(word)-1)//2])
        break