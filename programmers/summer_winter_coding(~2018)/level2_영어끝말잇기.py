def solution(n, words):
    answer = [0, 0]
    player, turn, last = 1, 1, words[0][0]
    word_set = set()
    while words:
        word = words.pop(0)
        if last != word[0] or word in word_set:
            return [player, turn]
        else:
            word_set.add(word)
            last = word[-1]
            player += 1
            if player > n:
                player -= n
                turn += 1
    return answer