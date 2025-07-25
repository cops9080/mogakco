secret_code, meeting_point, time = input().split()
time = int(time)

class Agent:
    def __init__(self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time

agent = Agent(secret_code, meeting_point, time)
print(f"secret code : {agent.s}")
print(f"meeting point : {agent.m}")
print(f"time : {agent.t}")