#########################
#  SWEA number 4839
#  by 김승현                
#########################

# Q. 이진  탐색

def binary_search(target, start, end, count):
    count += 1
    find = (start + end)//2
    if find == target:
        return count
    else:
        return binary_search(target, find, end, count) if find < target else binary_search(target, start, find, count)

for t in range(1, int(input())+1):
    end, pa, pb = map(int, input().split())
    count_a = binary_search(pa, 1, end, 0)
    count_b = binary_search(pb, 1, end, 0)
    if count_a == count_b:
        print("#%d 0" %t)
    else:
        print("#%d A" %t) if count_a < count_b else print("#%d B" %t)