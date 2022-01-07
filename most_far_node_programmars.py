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
    count_cost(cnt, adj_v, [0], costs, visited, n)
    max_len = max(costs)
    answer = 0
    for v in costs:
        if v == max_len:
            answer += 1
    return answer

def count_cost(cnt, adj_v, queue, costs, visited, n):
    if len(visited) == n:
        return 0
    new_queue = []
    cnt += 1
    for cur in queue:
        for candi in adj_v[cur]:
            if candi not in visited:
                visited.append(candi)
                costs[candi] = cnt
                new_queue.append(candi)
    count_cost(cnt, adj_v, new_queue, costs, visited, n)
    # print(costs)
    answer = 0
    return answer

sol = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)
print(sol)