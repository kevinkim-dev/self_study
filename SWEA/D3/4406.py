#########################
#  SWEA number 4406
#  by 김승현                
#########################

# Q. 모음이 보이지 않는 사람

vowels = ['a', 'e', 'i', 'o', 'u']

for t in range(1, int(input())+1):
    word = input()
    new_word = ''
    for char in word:
        if char not in vowels:
            new_word += char
    print("#%d %s" %(t, new_word))