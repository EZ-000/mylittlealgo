import sys
input = sys.stdin.readline

N = input()
arr1 = set(input().split())
M = input()
arr2 = input().split()

for n in arr2:
    if n in arr1:
        print(1)
    else:
        print(0)

'''참고:
List 자료형은 삽입, 제거, 탐색, 포함 여부 확인 모두
O(n)에 해당하는 시간 복잡도를 가지고 있습니다.

Set과 Dictionary는 삽입, 제거, 탐색, 포함여부확인 연산에
O(1)의 시간 복잡도를 가지고 있습니다.

탐색과 확인이 주로 필요한 연산이라면 Set이나 Dictionary를 사용하는 것이 좋고
순서와 index에 따른 접근이 필요하다면 List 자료형을 사용하는 것이 좋을 것입니다.

(출처: https://chancoding.tistory.com/43)
'''
