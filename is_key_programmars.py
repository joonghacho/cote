def turn_90(key):
    key_size = len(key)
    new_key = [[0 for _ in range(key_size)] for _ in range(key_size)]
    for j in range(key_size):
        for i in range(key_size):
            new_key[j][i] = key[key_size-1-i][j]
    return new_key

def get_True(the_map, key_size, lock_size):
    answer = True
    for j in range(lock_size):
        for i in range(lock_size):
            if the_map[j+key_size-1][i+key_size-1] != 1:
                answer = False
    return answer

def try_key(the_map, key, zero_x, zero_y):
    key_size = len(key)
    for j in range(key_size):
        for i in range(key_size):
            the_map[zero_y+j][zero_x+i] += key[j][i]
        
    answer = get_True(the_map, key_size, len(the_map) - 2*(key_size-1))
    for j in range(key_size):
        for i in range(key_size):
            the_map[zero_y+j][zero_x+i] -= key[j][i]
    return answer

def solution(key, lock):
    if len(lock) == 1 and (sum(key) + sum(lock) == 1):
        return True
    if len(lock) == 1 and (sum(key) + sum(lock) != 1):
        return False
    answer = False
    key_size = len(key)
    lock_size = len(lock)
    map_size = lock_size + 2*(key_size-1)
    the_map = [[0 for _ in range(map_size)] for _ in range(map_size)]
    for j in range(lock_size):
        for i in range(lock_size):
            the_map[j+key_size-1][i+key_size-1] = lock[j][i]
    # print("the_map:", the_map)
    for _ in range(4):
        key = turn_90(key)
        # print("key:", key)
        for j in range(key_size+lock_size-1):
            for i in range(key_size+lock_size-1):
                answer = try_key(the_map, key, i, j)
                if answer == True:
                    return True
    return answer

sol = solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 0], [1, 0, 0], [1, 0, 0]])
print(sol)