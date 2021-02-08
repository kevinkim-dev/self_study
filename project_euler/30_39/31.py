# ##########################
#  project_euler number 31
#  by 김승현                
# ##########################

# Q. 영국 화폐 액면가를 조합하는 방법의 수

pay_list = [200, 100, 50, 20, 10, 5, 2, 1]
pay_count = [0]*len(pay_list)
pay_way_count = 0

money = 200

for a in range(money // (pay_list[0]) + 1):
    for b in range(money // (pay_list[1]) + 1):
        if a*pay_list[0]+b*pay_list[1] > 200:
            break
        for c in range(money // (pay_list[2]) + 1):
            if a*pay_list[0]+b*pay_list[1]+c*pay_list[2] > 200:
                break
            for d in range(money // (pay_list[3]) + 1):
                if a*pay_list[0]+b*pay_list[1]+c*pay_list[2]+d*pay_list[3] > 200:
                    break
                for e in range(money // (pay_list[4]) + 1):
                    if a*pay_list[0]+b*pay_list[1]+c*pay_list[2]+d*pay_list[3]+e*pay_list[4] > 200:
                        break
                    for f in range(money // (pay_list[5]) + 1):
                        if a*pay_list[0]+b*pay_list[1]+c*pay_list[2]+d*pay_list[3]+e*pay_list[4]+f*pay_list[5] > 200:
                            break
                        for g in range(money // (pay_list[6]) + 1):
                            if a*pay_list[0]+b*pay_list[1]+c*pay_list[2]+d*pay_list[3]+e*pay_list[4]+f*pay_list[5]+g*pay_list[6] > 200:
                                break
                            for h in range(money // (pay_list[7]) + 1):
                                if a*pay_list[0]+b*pay_list[1]+c*pay_list[2]+d*pay_list[3]+e*pay_list[4]+f*pay_list[5]+g*pay_list[6]+h*pay_list[7] > 200:
                                    break
                                elif a*pay_list[0]+b*pay_list[1]+c*pay_list[2]+d*pay_list[3]+e*pay_list[4]+f*pay_list[5]+g*pay_list[6]+h*pay_list[7] == 200:
                                    pay_way_count += 1
                                    print("%d %d %d %d %d %d %d %d" % (a, b, c, d, e, f, g, h))

print(pay_way_count)










# 2원을 1원으로 조합하는 방법
# 5원을 2원과 1원으로 조합하는 방법 -> 2원을 1원으로 조합하는 방법 * 2 + 1
# 10원을 5원과 2원과 1원으로 조합하는 방법 -> 5원을 2원으로 조합하는 방법 * 2 + 1
# 20원을 10원과 5, 2, 1원으로 조합하는 방법 -> 10원을 5, 2, 1원으로 조합하는 방법 * 2 + 1
# 50원을 20~1원 조합 -> 20원을 10~조합하는 방법 * 2 + 1

# count = 1

# for i in range(6):
#     count = 2*count + 1

# print(count+1)
