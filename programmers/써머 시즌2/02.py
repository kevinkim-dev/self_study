#########################
#  Programmers problem kit 
#  summer 05월
#  by 김승현                
#########################

# Q. 2번

def solution(numbers):
    answer = []
    for number in numbers:
        if len(bin(number)) >= 5 and len(bin(number).split('0')[-1]) >= 3:
            x = len(bin(number).replace('b', '0').split('0')[-1])
            answer.append(number + 2**(x-1))
        else:
            new_num = number + 1
            while True:
                result = list(map(int, list(bin(number ^ new_num)[2:])))
                if sum(result) <= 2:
                    answer.append(new_num)
                    break
                new_num += 1
    return answer

numbers = list(range(15))
print(solution(numbers))

# def solution(numbers):
#     answer = []
#     for number in numbers:
#         new_num = number + 1
#         while True:
#             result = list(map(int, list(bin(number ^ new_num)[2:])))
#             if sum(result) <= 2:
#                 answer.append(new_num)
#                 break
#             new_num += 1
#     return answer

# numbers = [2, 7]
# print(solution(numbers))