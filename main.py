# Solution
def solution(S):
    # 'a' 또는 'A'가 두번 이상 연속되는 부분 문자열을 찾아 'a'로 치환한다.

    T = ""
    i = 0

    # while 문을 이용하여 문자열 S의 원소 하나씩 탐색
    while i < len(S):
        # 탐색하는 원소가 'a' , 'A'가 아니라면 문자열 T에 추가
        if S[i] != 'a' and S[i] != 'A':
            T += S[i]
            i += 1
            continue

        # 탐색하던 원소가 'a' , 'A'면 그 뒤에 부분문자열이 얼마나 있는지 탐색
        j = i + 1

        while j < len(S):
            # i번째 원소 뒤로 'a', 'A'가 아닌 문자가 있을 떄까지
            if S[j] != 'a' and S[j] != 'A':
                break
            j += 1

        #뒤에 다른 문자열이 있다면 바로 추가
        if j - i == 1:
            T += S[i]
        else:
            T += S[i].lower()

        i = j

    return T

# input
S = input().strip()
print(solution(S))
