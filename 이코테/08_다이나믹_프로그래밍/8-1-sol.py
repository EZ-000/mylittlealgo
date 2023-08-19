import time
start = time.time()

X = int(input())
dp = [0] * 30001
# 2부터 연산하며 dp 테이블 채우기
# dp 테이블에 채워지는 값 == 그 idx까지 사용하는 연산의 최소 횟수
for x in range(2, X + 1):
    dp[x] = dp[x - 1] + 1
    if not x % 2:
        dp[x] = min(dp[x], dp[x // 2] + 1)
    if not x % 3:
        dp[x] = min(dp[x], dp[x // 3] + 1)
    if not x % 5:
        dp[x] = min(dp[x], dp[x // 5] + 1)

print(dp[x])
print(time.time() - start)
