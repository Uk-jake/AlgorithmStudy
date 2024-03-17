n, m = map(int, input().strip().split())

dic = {}

for i in range(5):
    key, value = map(str, input().strip().split())
    dic[key] = int(value)

array = input().strip().split()

result = 0

for a in array:
    result = result + dic[a]

print(result)
print(result)
