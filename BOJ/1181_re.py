# 시간 초과 ㅠㅠ
import sys

# sort 메서드를 안 쓰기 위해 버블 정렬을 이용
N = int(sys.stdin.readline())
# key가 알파벳 문자이고 value가 숫자인 dict 생성
alphabet = list('abcdefghijklmnopqrstuvwxyz')
asc_dict = {}
for idx in range(26):
    asc_dict[alphabet[idx]] = idx

# 단어가 길이별로 들어갈 이중 리스트 생성
# 조건: 문자열의 길이가 50을 넘지 않는다.
words = [[] for _ in range(50)]
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words[len(word) - 1].append(word)

for i in range(50):
    # 단어 중복 제거
    words[i] = set(words[i])
    words[i] = list(words[i])
    # 그 길이의 단어가 없는 경우에 스킵
    if len(words[i]) == 0:
        continue
    else:
        # 단어의 k 번째 글자를 기준으로 버블 정렬
        for j in range(len(words[i]) - 1, 0, -1):
            for k in range(i + 1):
                for w in range(0, j):
                    # k가 첫 번째 글자일 경우
                    if k == 0:
                        if asc_dict[words[i][w][k]] > asc_dict[words[i][w + 1][k]]:
                            words[i][w], words[i][w + 1] = words[i][w + 1], words[i][w]
                    # k가 첫 번째 글자가 아닐 경우 앞 글자가 같은 경우만 버블 정렬
                    else:
                        if words[i][w][k - 1] == words[i][w + 1][k - 1]:
                            if asc_dict[words[i][w][k]] > asc_dict[words[i][w + 1][k]]:
                                words[i][w], words[i][w + 1] = words[i][w + 1], words[i][w]

for i in range(50):
    if len(words[i]) > 0:
        for j in range(len(words[i])):
            print(words[i][j])
