#########################
#  SWEA number 4008
#  by 김승현                
#########################

# Q. 숫자 만들기

# 1. 연산자 고르기
# 2. 계산
# 3. 연산자 -1

# 연산자 섞기
# 덧셈, 뺄셈, 곱셈, 나눗셈 순으로 배치

def op_combintation(op_cnt, nums):
    global min_num, max_num
    if len(nums) == 1:
        min_num = min(min_num, nums[0])
        max_num = max(max_num, nums[0])
        return
    x = nums.pop()
    y = nums.pop()
    for i in range(4):
        if op_cnt[i] != 0:
            op_combintation(op_list_modify(op_cnt, i), nums + [operate(x, y, i)])
def op_list_modify(op_cnt, num):
    temp_list = op_cnt[:]
    temp_list[num] -= 1
    return(temp_list)

def operate(a, b, op_num):
    if op_num == 0:
        return a + b
    elif op_num == 1:
        return a - b
    elif op_num == 2:
        return a * b
    else:
        return int(a/b)
    

for t in range(1, int(input())+1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    min_num = float('inf')
    max_num = float('-inf')
    op_com = [0]*(N-1)
    num_list = list(map(int, input().split()))[::-1]
    op_combintation(op_cnt, num_list)
    print("#%d %d" %(t, max_num - min_num))

# # 1. 연산자 섞기
# # 2. 나눗셈 처리 로직
# # 3. stack형으로 operate

# # 연산자 섞기
# # 덧셈, 뺄셈, 곱셈, 나눗셈 순으로 배치
# def op_combintation(op_list, op_com):
#     while op_list:
#         op = op_list.pop(0)
#         for idx in range(N-1):
#             if op_com[idx] = 0:
#                 op_combintation(op_list, )


# def operate():
#     pass

# for t in range(1, int(input())+1):
#     N = int(input())
#     op_cnt = [0] + list(map(int, input().split()))
#     op_list = []
#     for i in range(1, 5):
#         if op_cnt[i]:
#             op_list += [i]*op_cnt[i]
#     print(op_cnt)
#     print(op_list)
#     op_com = [0]*(N-1)
#     num_list = list(map(int, input().split()))
