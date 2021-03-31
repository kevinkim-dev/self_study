#########################
#  SWEA number 1759
#  by 김승현                
#########################

# Q. 암호 만들기

from itertools import combinations

L, C = map(int, input().split())
non_vowels = sorted(input().split())
vowels = []
passwords = []
for al in non_vowels:
    if al in {'a', 'e', 'i', 'o', 'u'}:
        vowels.append(al)
non_vowels = list(set(non_vowels) - set(vowels))
for non_vowel_num in range(2, len(non_vowels)+1):
    vowel_num = L - non_vowel_num
    if 1 <= vowel_num <= len(vowels):
        for comb1 in combinations(range(len(non_vowels)), non_vowel_num):
            passw = [non_vowels[i] for i in comb1]
            for comb2 in combinations(range(len(vowels)), vowel_num):
                password = passw[:]
                for j in comb2:
                    password.append(vowels[j])
                passwords.append(''.join(sorted(password)))
for password in sorted(passwords):
    print(password)
                