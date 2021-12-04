###########################
#  BaekJoon 2587번
#  by 김승현                
###########################

# Q. 대표값2

num_list = []

for _ in range(5):
    num_list.append(int(input()))

print(sum(num_list)//5)
print(sorted(num_list)[2])