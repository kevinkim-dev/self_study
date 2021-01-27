# ##########################
#  project_euler number 18
#  by 김승현                
# ##########################

# Q. 20세기에서, 매월 1일이 일요일인 경우는 몇 번?

# 매 년 1월 1일을 체크한다.
# 매 월 1일을 체크하여 7로 나눠서 나머지가 6이면 일요일

jan_first_list = []
month_first_list = []

not_yundal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
yundal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

for i in range(100):
    if i == 0:
        jan_first_list.append(365)
    elif i % 4 ==0:
        jan_first_list.append(jan_first_list[i-1] + 366)
    else:
        jan_first_list.append(jan_first_list[i-1] + 365) 


for i, jan_first in enumerate(jan_first_list):
    temp = [jan_first]
    if i == 0 or i % 4 != 3:
        for j in not_yundal:
            jan_first += j
            temp.append(jan_first)
        month_first_list.append(temp)
    else:
        for j in yundal:
            jan_first += j
            temp.append(jan_first)
        month_first_list.append(temp)
    # print(f"{1901 + i}년 1일 = {temp}")
count = 0 

for year_month in month_first_list:
    for month_first in year_month:
        if month_first % 7 == 6:
            count += 1  

print(count)      
