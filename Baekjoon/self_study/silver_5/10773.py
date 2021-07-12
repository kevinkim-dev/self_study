###########################
#  BaekJoon 10773번
#  by 김승현                
###########################

# Q. 제로

answer = []

for _ in range(int(input())):
    num = int(input())
    if num:
        answer.append(num)
    else:
        answer.pop()

print(sum(answer))