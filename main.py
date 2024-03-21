#Solution
def solution(A, B):

    C = []

    for b in B:
        count = 0
        for a in A:
            if b <= a:
                count += 1
        C.append(count)

    for c in C:
        print(c)



# input
n, m = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
#B = []
#for i in range(m):
#    B.append(int(input().strip()))
B = list(int(input().strip()) for _ in range(m))

solution(A,B)