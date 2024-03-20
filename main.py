import queue
#Solution
def solution(n, S):

    que1 = queue.Queue()
    que2 = queue.Queue()
    A,B,C = [],[],[]

    for item in S:
        if item[0] == 1:
            que1.put(item[1])
            que2.put(item[2])
        elif item[0] == 2:
            # item[1] - 준비된 음식 종류
            number = que1.get()
            want = que2.get()
            if item[1] == want:
                A.append(number)
            else :
                B.append(number)

    if que1.qsize() > 0:
        for i in range(que1.qsize()):
            C.append(que1.get())
        C.sort()
    elif que1.qsize() == 0:
        C.append("None")

    A.sort()
    B.sort()

    for a in A:
        print(f"{a}", end=" ")
    print("")
    for b in B:
        print(f"{b}", end=" ")
    print("")
    for c in C:
        print(f"{c}", end=" ")

# input
n = int(input())
S = list(list(map(int, input().strip().split())) for _ in range(n))

solution(n,S)
