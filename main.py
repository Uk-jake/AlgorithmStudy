import queue

#Solution
def solution(A, B):

    que = queue.Queue()
    mx, number = 0, A

    for i in range(A):
        if B[i][0] == 1:
            que.put(B[i][1])
            if mx < que.qsize() or (mx == que.qsize() and number > B[i][1]):
                mx = que.qsize()
                number = B[i][1]
        elif B[i][0] == 2:
            que.get()

    print(mx, number)

# input
A = int(input())
B = list(list(map(int, input().strip().split())) for _ in range(A))

solution(A,B)
