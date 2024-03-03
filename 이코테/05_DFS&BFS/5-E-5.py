# 반복으로 구현한 n!
def factorial_iterative(n):
    result = 2
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀로 구현한 n!
def factorial_recursive(n):
    if n <= 1:    # n이 1 이하인 경우 1을 반환
        print(n, '이 1 이하이므로 1을 리턴합니다.')
        return 1
    # n! = n * (n - 1)!
    print(n, '에', n - 1, '의 팩토리얼을 곱합니다.')
    n *= factorial_recursive(n - 1)
    print('리턴 값은', n, '입니다.')
    return n


print(factorial_recursive(5))
