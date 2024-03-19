#Solution
def solution(A, B):

    dict = {}
    mx = 0

    for b in B:
        if b in dict:
            dict[b] += 1
        else:
            dict[b] = 1
        #max 함수 사용
        mx = max(mx,dict[b])

    result = []

    # dict.item()의 출력 결과는 key,value 값을 2차원 리스트로 반환함.
    # for에 2차원 리스트를 사용하면 한 행의 2개의 열 값을 인자로 사용 가능 함.
    for key, value in dict.items():
        if value == mx:
            result.append(key)

    result.sort()

    for i in result:
        print(f"{i}", end=" ")

# input
A = int(input())
B = list(map(int, input().strip().split()))

solution(A,B)
