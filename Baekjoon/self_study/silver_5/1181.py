###########################
#  BaekJoon 1181번
#  by 김승현                
###########################

# Q. 단어 정렬

N = int(input())
word_set = set()
for n in range(N):
    word_set.add(input())
word_list = sorted(list(word_set))

for n in range(50):
    for word in word_list:
        if len(word) == n+1:
            print(word)
    






# def dictionary(word_set, length):
#     l = len(word_set)
#     for i in range(l-1, 0, -1):
#         for j in range(i):
#             for word_len in range(length):
#                 if ord(word_set[j][word_len]) > ord(word_set[j+1][word_len]):
#                     word_set[j], word_set[j+1] = word_set[j+1], word_set[j]
#                     break
#                 elif ord(word_set[j][word_len]) < ord(word_set[j+1][word_len]):
#                     break
#     return word_set



# N = int(input())
# words = [set() for _ in range(51)]
# for n in range(N):
#     word = input()
#     words[len(word)].add(word)
# for length in range(51):
#     sorted_set = dictionary(list(words[length]), length)
#     for word in sorted_set:
#         print(word)

