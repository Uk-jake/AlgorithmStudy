#Solution
def solution(A, B):

    dict = {}

    for a in A:
        for i in range(len(a) - 1):
            x = a[:i + 1]
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1

    if B in dict:
        print(dict[B])
    else:
        print(0)

# input
A = list(input().strip().split())
B = input()

solution(A,B)
