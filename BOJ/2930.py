import sys
input = lambda: sys.stdin.readline().rstrip()


Round = int(input())
SG = list(input())
N = int(input())

S = [0] * Round
P = [0] * Round
R = [0] * Round

win = [('S', 'P'), ('P', 'R'), ('R', 'S')]
tie = [('S', 'S'), ('P', 'P'), ('R', 'R')]

score = 0
for _ in range(N):
    F = list(input())
    for idx in range(Round):
        if (SG[idx], F[idx]) in win:
            score += 2
        elif (SG[idx], F[idx]) in tie:
            score += 1

        if F[idx] == 'S':
            S[idx] += 1
        elif F[idx] == 'P':
            P[idx] += 1
        elif F[idx] == 'R':
            R[idx] += 1

max_score = 0
for idx in range(Round):
    ifs = S[idx] + P[idx] * 2
    ifp = P[idx] + R[idx] * 2
    ifr = R[idx] + S[idx] * 2
    max_score += max(ifs, ifp, ifr)

print(score)
print(max_score)
