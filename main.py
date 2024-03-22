# Solution
def solution(A, B):
    for b in B:
        if b[0] == 1:
            add_k(A, b[1], b[3], b[2], b[4], b[5])
        elif b[0] == 2:
            count = 0
            for i in range(b[1], b[3] + 1):
                for j in range(b[2], b[4] + 1):
                    count += A[i][j]
            print(count)


def add_k(A, a, b, c, d, k):
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            A[i][j] += k

# input
n, m = map(int, input().strip().split())
A = list(list(map(int, input().strip().split())) for _ in range(n))
B = list(list(map(int, input().strip().split())) for _ in range(m))

# print(n, m)
# print(A)
# print(B)

solution(A, B)
