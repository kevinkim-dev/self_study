#########################
#  SWEA number 2050  
#  by 김승현                
#########################

# Q. 알파벳을 숫자로 변환

# string을 input으로 받아온다
string = input()
# string의 각 글자를 숫자로 바꿔서 저장할 list 초기화
string_num = []

for i in string:
    # ASCII 코드 상에서 A는 65로 시작해서 1씩 증가하므로
    # 각 글자의 ASCII 코드에 -64를 하면 1~26이 출력
    string_num.append(str(ord(i)-64))

# list안의 str element를 공백으로 구분하여 출력
print(" ".join(string_num))