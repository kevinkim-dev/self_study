###########################
#  BaekJoon 3052번
#  by 김승현                
###########################

# Q. 나머지

num_set = set()
for t in range(10):
    num_set.add(int(input()) % 42)

print(len(num_set))