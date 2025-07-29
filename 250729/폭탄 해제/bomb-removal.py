unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Bomb:
    def __init__(self, unlock_code, wire_color, seconds):
        self.code = unlock_code
        self.color = wire_color
        self.sec = seconds
    
bomb1 = Bomb(unlock_code, wire_color, seconds)

print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.sec}")