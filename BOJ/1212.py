import sys
input = sys.stdin.readline

octa = input()
deci = 0
lenO = len(octa)
lenB = 3 * len(octa) + 1
bina = ''

for i in range(lenO):
    deci += int(octa[i]) * 8 ** (lenO - i - 1)
for i in range(lenB):
    bina += '1' if deci & (1 << i) else '0'
print(bina.lstrip('0'))
