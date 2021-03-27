n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    print("target" + str(target))
    print("result" + str(result))
    n = target
    if n < k:
        break

    result += 1
    n //= k


result += (n-1)
print(result)