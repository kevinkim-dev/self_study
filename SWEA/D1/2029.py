#########################
#  SWEA number 2029  
#  by 김승현                
#########################

# Q. 몫과 나머지 출력하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"#{test_case} {a // b} {a % b}")