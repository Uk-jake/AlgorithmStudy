#Solution
def solution(A, B):

    C = []

    for b in B:
        if b[0] == 1:
            for i in range(b[1],b[2]+1):
                A[i] += b[3]
        elif b[0] == 2:
            count = 0
            for a in A[b[1]:b[2]+1]:
                count += a
            C.append(count)

    return C


# input
n , m = map(int, input().strip().split())
A = list(map(int,input().strip().split()))
B = list(list(map(int,input().strip().split())) for _ in range(m))

# print(n, m)
# print(A)
# print(B)

answer = solution(A,B)

for item in answer:
    print(item)