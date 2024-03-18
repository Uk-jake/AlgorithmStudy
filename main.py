#Solution
def solution(S):

    # 이름 순서래도 오른차순으로 정렬
    S.sort()

    # 딕셔너리 초기화
    dict = {}

    # 딕셔너리에 하나씩 추가하면서 이미 존재하면 value 1씩 증가
    for key in S:
        if key in dict:
            dict[key] += 1
        else :
            dict[key] = 1

    for key in dict:
        print(f"{key} {dict[key]}")

# input
S = list(input().strip().split())

solution(S)
