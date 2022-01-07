def solution(n, edge):
    adj_v = [[] for _ in range(n)]
    for elements in edge:
        adj_v[elements[0]-1].append(elements[1]-1)
        adj_v[elements[1]-1].append(elements[0]-1)
    # print(vertexs)
    costs = [[] for _ in range(n)]
    costs[0] = 0
    visited = [0]
    cnt = 0
    queue = [0]
    while queue:
        if len(visited) == n:
            break
        cnt += 1
        new_queue = []
        for candi in queue:
            for ele in adj_v[candi]:
                if ele not in visited:
                    visited.append(ele)
                    costs[ele] = cnt
                    new_queue.append(ele)
        queue = new_queue   

    max_len = max(costs)
    answer = 0
    for v in costs:
        if v == max_len:
            answer += 1
    return answer

sol = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)
print(sol)