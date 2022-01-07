import sys
sys.setrecursionlimit(10**6)

def get_child(my_word, words, friends):
    for candi in words:
        count = 0
        for ele_i in range(len(my_word)):
            if candi[ele_i] == my_word[ele_i]:
                count += 1
        if count == len(my_word) - 1:
            friends.append([my_word, candi])
    return 0

def change_fri_num(whole_words, friends):
    for i, word in enumerate(whole_words):
        for friend in friends:
            for man in range(2):
                if friend[man] == word:
                    friend[man] = i
    return friends

def get_adj(whole_words, friends):
    adj_list = [[] for _ in range(len(whole_words))]
    for f in friends:
        adj_list[f[0]].append(f[1])
    return adj_list

def get_short_change(adj_list, n):
    visited = [False] * n
    visited[0] = True
    count = 0
    queue = [0]
    while visited[-1] == False:
        new_queue = []
        for i in queue:
            for j in adj_list[i]:
                new_queue.append(j)
                visited[j] = True
        queue = new_queue
        count += 1
    return count

def solution(begin, target, words):
    if target not in words:
        return 0
    whole_words = [begin] + words
    whole_words.remove(target)
    whole_words.append(target)
    w_len = len(whole_words)
    friends = []
    for word in whole_words:
        get_child(word, whole_words, friends)
    # print(friends)
    change_fri_num(whole_words, friends)
    adj_list = get_adj(whole_words, friends)
    # print(adj_list)
    # print(friends)
    answer = get_short_change(adj_list, w_len)
    return answer

sol = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(sol)