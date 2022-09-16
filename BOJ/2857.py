agents = []
for idx in range(5):
    agent = input()
    if len(agent) < 11 and 'FBI' in agent:
        agents += [idx + 1]

if agents:
    print(*agents)
else:
    print('HE GOT AWAY!')
