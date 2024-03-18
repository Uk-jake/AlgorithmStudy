#Solution
def solution(A, B):

    dict = {}

    for b in B:
        dict[b] = 1

    C = []

    for a in A:
        if a not in dict:
            C.append(a)

    C.sort()

    for c in C:
        print(c)

# input
A = list(input().strip().split())
B = list(input().strip().split())

solution(A,B)
