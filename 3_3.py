n, k = map(int, input().split())
result = 0

#n이 k보다 크거나 같을 경우에 반복
while n >= k:
    #n이 k로 나누어 떨어지지 않으면 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

#n이 1일 때까지
while n > 1:
    n -= 1
    result += 1

print(result)