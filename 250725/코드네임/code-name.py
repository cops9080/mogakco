MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class AgentInfor:
    def __init__(self, codename='', score=0):
        self.c = codename
        self.s = score
    
    def __str__(self):
        return f"{self.c} {self.s}"

agents = [AgentInfor() for _ in range(MAX_N)]

for i in range(0, 5):
    agents[i].c = codenames[i]
    agents[i].s = scores[i]

sorted_scores = list(sorted(scores))

for i in range(0, 5):
    if sorted_scores[0] == agents[i].s:
        tmp = i
        break

print(f"{agents[tmp].c} {agents[tmp].s}")