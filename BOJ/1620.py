import sys
input = lambda: sys.stdin.readline().rstrip()


def isPokemon(n):
    if 64 < ord(temp[0]) < 91:
        for c in temp[1:]:
            if not 96 < ord(c) < 123:
                return False
        else:
            return True
    elif 64 < ord(temp[-1]) < 91:
        for c in temp[1:]:
            if not 96 < ord(c) < 123:
                return False
        else:
            return True


N, M = map(int, input().split())
pokemons = {}
for idx in range(1, N + 1):
    name = input()
    pokemons[str(idx)] = name
    pokemons[name] = idx

for _ in range(M):
    Q = input()
    print(pokemons[Q])
