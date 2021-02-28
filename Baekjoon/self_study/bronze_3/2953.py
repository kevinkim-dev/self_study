###########################
#  BaekJoon 2953번
#  by 김승현                
###########################

# Q. 나는 요리사다

max_sum = 0
for t in range(1, 6):
    x = sum(list(map(int, input().split())))
    if x > max_sum:
        max_sum = x
        max_index = t
print(max_index, max_sum)