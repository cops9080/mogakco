user2_id, user2_level = input().split()
user2_level = int(user2_level)

class Infor:
    def __init__(self, user2_id, user2_level=0):
        self.ids = user2_id
        self.lvl = user2_level

user1 = Infor('codetree', 10)
user2 = Infor(user2_id, user2_level)

print(f"user {user1.ids} lv {user1.lvl}")
print(f"user {user2.ids} lv {user2.lvl}")