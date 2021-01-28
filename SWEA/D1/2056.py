#########################
#  SWEA number 2056  
#  by 김승현                
#########################

# Q. 연월일 달력

T = int(input())

for i in range(1, T+1):
    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    s_year = date[0:4]
    s_month = date[4:6]
    s_day = date[6:8]
    if month < 1 or month > 12 or day < 1:
        print(f"#{i} -1")
    elif month == 2 and day > 28:
        print(f"#{i} -1")
    elif (month == 1 or month == 3 or month == 5 or 
    month == 7 or month == 8 or month == 10 
    or month == 12) and day > 31:
        print(f"#{i} -1")
    elif (month == 4 or month == 6 or month == 9 or 
    month == 11) and day > 30:
        print(f"#{i} -1")
    else:
        print(f"#{i} {s_year}/{s_month}/{s_day}")
    # 출력 두번째 방법
    # print(f"#{i} {str(year).rjust(4, '0')}/{str(month).rjust(2, '0')}/{str(day).rjust(2, '0')}")
        