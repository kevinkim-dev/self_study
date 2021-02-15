###########################
#  BaekJoon 11943번
#  by 김승현                
###########################

# Q. 파일 옮기기

a_a, a_o = map(int, input().split())
b_a, b_o = map(int, input().split())

case_1 = a_a + b_o
case_2 = a_o + b_a

print(case_1) if case_1 < case_2 else print(case_2)