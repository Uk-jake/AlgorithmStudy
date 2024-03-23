# Solution
def solution(A):

    time = [0] * 3600

    for a in A:
        if a[0] == '1':
            t1 = translate_time(a[1])
            t2 = translate_time(a[2])
            for i in range(t1, t2):
                time[i] += 1

        elif a[0] == '2':
            t1 = translate_time(a[1])
            print(time[t1])

    return 0

def translate_time(t):
    return int(t[:2])*60 + int(t[3:])

# input
n = int(input().strip())
A = list(input().strip().split() for _ in range(n))

solution(A)