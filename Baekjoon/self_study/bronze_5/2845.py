###########################
#  BaekJoon 2845번
#  by 김승현                
###########################

# Q. 파티가 끝나고 난 뒤

L, P = map(int, input().split())
people = L * P

article_list = list(map(int, input().split()))
for i in range(len(article_list)):
    article_list[i] = str(article_list[i]-people)

ans = " ".join(article_list)
print(ans)