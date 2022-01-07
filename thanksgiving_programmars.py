def get_head_tail(line):
    for_long = line[24:-1]
    long = int(1000*float(for_long))
    end = 1000*60*60*(int(line[11:13])) + 1000*60*(int(line[14:16])) + 1000*int(line[17:19]) + int(line[20:23])
    start = end - long + 1
    return [start, end]

def get_logs_at_time(time, head_tail_set):
    count = 0
    for one_set in head_tail_set:
        if (time <= one_set[0] <= time + 999) or (time <= one_set[1] <= time + 999) or (one_set[0] < time and one_set[1] > time + 999):
            count += 1
    return count

def solution(lines):
    head_tail_set = []
    time_candidate = []
    for line in lines:
        one_log = get_head_tail(line)
        head_tail_set.append(one_log)
        time_candidate.append(one_log[0])
        time_candidate.append(one_log[1])
    answer = 0
    for time in time_candidate:
        # print("time: ", time)
        answer_candi = get_logs_at_time(time, head_tail_set)
        if answer_candi > answer:
            answer = answer_candi
    # print("print(head_tail_set)", head_tail_set)
    return answer

a = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

sol = solution(a)
print(sol)

