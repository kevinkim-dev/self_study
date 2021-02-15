###########################
#  BaekJoon 11948번
#  by 김승현                
###########################

# Q. 과목선택

_sum = 0
min_science = float('inf')
min_social = float('inf')
for n in range(4):
    x = int(input())
    if x < min_science:
        min_science = x
    _sum += x
_sum -= min_science

for n in range(2):
    x = int(input())
    if x < min_social:
        min_social = x
    _sum += x
_sum -= min_social

print(_sum)