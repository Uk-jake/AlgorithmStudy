# Solution
def solution(S):
    return sorted(S)

# input
S = input().strip()
print(S, type(S))

# sorted() - 파이썬 표준 내장 함수 : 정렬
#   새로운 정렬 결과 반환, 원래 목록에 영향 X

# sort() - 리스트 메서드 : 정렬 -> str형태에는 사용할 수 없음.
#   기존 리스트의 값들을 정렬해주는 기능, 반환 값 없음.
answer = sorted(S)

for s in answer:
    print(f"{s}" , end="")