#Solution
def solution(A, B):

    dict = {}
    C = []

    for a in A:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1

    for b in B:
        if b in dict:
            C.append(dict[b])
        else:
            C.append(len(A))

    return C

# input
n, m = map(int,input().strip().split())
answer = list(input().strip().split())
question = list(input().strip() for _ in range(m))

result = solution(answer,question)

for item in result:
    print(item)