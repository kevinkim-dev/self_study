# ##########################
#  project_euler number 24
#  by 김승현                
# ##########################

# Q. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 1,000,000번째 사전식 순열은?

# for i in range(1, 12):
#     fact = 1
#     for j in range(1, i+1):
#         fact *= j
#     print(f"{i}! = {fact}")

# index = int(input())

def factorial(x):
    result = 1
    for n in range(1, x+1):
        result *= n
    return result

# 0~9 num_list에서 사용된 숫자를 하나씩 뺄 것이다
num_list = []
for i in range(10):
    num_list.append(i)

index = 1000000

lexicographic_num = ''
while index > 1:
    for n in range(9, 0, -1):
        count = 0
        fact = factorial(n)
        while index > fact:
            index -= fact
            count += 1
        lexicographic_num += str(num_list[count])
        print(f"remove {num_list[count]}")
        num_list.remove(num_list[count])
lexicographic_num += str(num_list[0])
print(lexicographic_num)