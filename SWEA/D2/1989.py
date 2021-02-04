#########################
#  SWEA number 1989 
#  by 김승현                
#########################

# Q. 초심자의 회문 검사

# T = int(input())

# for t in range(1, T+1):
#     # 회문인지 아닌지 판단할 flag. 일단 1
#     flag = 1
#     string = input()
#     # string이 없어질 때까지 반복 
#     # 첫자리와 끝자리가 같은지 확인 후 slicing으로 반복
#     while string:
#         if string[0] == string[-1]:
#             string = string[1:-1]
#         # 회문이 아니라면 flag를 0으로 바꾸고 0 출력 후 break로 빠져나감
#         else:
#             print(f"#{t} 0")
#             flag = 0
#             break
#     # 회문이었다면 flag 이상없이 while문 종료하므로 출력
#     # 회문이 아니었다면 flag가 0이므로 출력하지 않음
#     if flag == 1:
#         print(f"#{t} 1")


# flag 없이 풀고 싶다면 함수를 정의해서 return으로 빠져나가도 된다.

def palindrome(string):
    while string:
        if string[0] == string[-1]:
            string = string[1:-1]
        else:
            return 0
    return 1

T = int(input())

for t in range(1, T+1):
    print(f"#{t} {palindrome(input())}")