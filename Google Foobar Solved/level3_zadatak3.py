def solution(l):
    out = 0
    pair_counts = [0] * len(l)
    for i in range(1, len(l) - 1):
        for j in range(i):
            if l[i] % l[j] == 0:
                pair_counts[i] += 1
    print("pairs counts->",pair_counts)
    for i in range(2, len(l)):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                out += pair_counts[j]
    return out





print(solution([1,2,3,4,5]))



'''
def solution(l):
    out = 0
    pair_counts = [0] * len(l)
    for i in xrange(1, len(l) - 1):
        for j in xrange(i):
            if l[i] % l[j] == 0:
                pair_counts[i] += 1
    for i in xrange(2, len(l)):
        for j in xrange(1, i):
            if l[i] % l[j] == 0:
                out += pair_counts[j]
    return out


'''
