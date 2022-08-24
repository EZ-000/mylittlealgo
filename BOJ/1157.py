import sys
input = lambda: sys.stdin.readline().rstrip()

word = input().upper()
cnt = {}
for c in word:
    if c in cnt.keys():
        cnt[c] = cnt[c] + 1
    else:
        cnt[c] = 1

temp = 0
max_cnt = []
for key, val in cnt.items():
    if temp < val:
        temp = val
        max_cnt = [key, val]
    elif temp == val:
        max_cnt += [key, val]

if len(max_cnt) == 2:
    print(max_cnt[0])
else:
    print('?')

'''mini_log
내가 작성한 것 중에 제일 실행 시간이 짧았던 코드다.
그래도 너무 실행 시간이 길어서 참고 코드를 같이 남겨둔다.

i = input().upper()
n = 0
for p in map(chr, range(65, 91)):
    q = i.count(p)
    if n < q:
        n, c = q, p
    elif n == q:
        c = '?'
print(c)

이렇게 하면 불필요한 데이터를 더 저장하지도 않고, for문도 줄어든다.
그리고 아마 테스트케이스 중에 굉장히 긴 문자열이 주어지는 것도 있는 것 같은데,
그런 경우에 문자열 전체를 순회하는 내 방법보다 아스키 코드 변환을 이용해
대문자 값만 순환하는 코드들이 더 빠른 것 같다.
'''
