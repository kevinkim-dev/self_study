###########################
#  BaekJoon 15474번
#  by 김승현                
###########################

# Q. 鉛筆 (Pencils)

from math import ceil

N, A, B, C, D = map(int, input().split())

print(min(ceil(N/A)*B, ceil(N/C)*D))