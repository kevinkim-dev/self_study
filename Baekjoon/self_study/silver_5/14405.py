###########################
#  BaekJoon 14405번
#  by 김승현                
###########################

# Q. 피카츄

import sys

input = sys.stdin.readline

word = input().strip()

new_word = word.replace('pi', '1').replace('ka', '1').replace('chu', '1')

if len(new_word) == new_word.count('1'):
    print('YES')
else:
    print('NO')