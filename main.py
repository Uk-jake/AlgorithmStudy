#Solution
def solution(n, m, dict, b):
    result = 0

    for item in b:
        if item in dict:
            result = result + dict[item]

    return result

# input
n, m = map(int, input().strip().split())

dict = {}

for i in range(n):
    name, price = input().strip().split()
    dict[name] = int(price)

b = list(input().strip().split())

print(solution(n,m,dict,b))
