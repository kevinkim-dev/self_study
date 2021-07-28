###########################
#  BaekJoon 10808번
#  by 김승현                
###########################

# Q. 알파벳 개수

alp = [0]*26

for c in input():
    alp[ord(c)-97] += 1
alp = list(map(str, alp))

print(' '.join(alp))