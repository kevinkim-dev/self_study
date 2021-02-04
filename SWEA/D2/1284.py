#########################
#  SWEA number 1284 
#  by 김승현                
#########################

# Q. 수도 요금 경쟁

# A: 1리터당 P
# B: 기본 Q, 월간사용량 R이하 는 Q, R 초과시, 초과량은 1리터당 S
# w: 사용 수도량

T = int(input())

for t in range(1, T+1):
    # 5개의 숫자를 받아와서 list로 작성
    variables = list(map(int, input().split()))
    # A회사 가격은 S * P
    A_cost = variables[4]*variables[0]
    # B회사 가격은 기준치 R에서 분기 한다
    # 기준치보다 많으면 차이만큼에 S를 곱해서 구한다.
    if variables[4] > variables[2]:
        B_cost = variables[1] + (variables[4] - variables[2]) * variables[3]
    else:
        B_cost = variables[1]
    # 둘 중 싼 가격을 출력한다
    print(f"#{t} {A_cost}") if A_cost < B_cost else print(f"#{t} {B_cost}")

