import itertools

# Solution
def solution(A):

    per = list(itertools.permutations(A,len(A)))
    answer = []

    for item in per:
        tmp = ''.join(item)
        answer.append(tmp)

    answer.sort()

    for a in answer:
        print(a)



# input
A = list(input().strip())
solution(A)