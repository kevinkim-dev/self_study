###########################
#  BaekJoon 4358번
#  by 김승현                
###########################

# Q. 생태학

import sys

input = sys.stdin.readline

tree_dict = dict()
total = 0

while True:
    tree = input().strip()
    if not tree:
        break
    tree_dict[tree] = tree_dict.get(tree, 0) + 1
    total += 1

for tree in sorted(tree_dict.keys()):
    print(f"{tree} %.4f" %(tree_dict.get(tree)*100/total))