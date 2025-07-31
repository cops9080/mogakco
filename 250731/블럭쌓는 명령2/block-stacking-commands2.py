n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

blocks = [0] * (n+1)
start = 0
end = 0
for i in range(0, k):
    start, end = commands[i]
    for i in range(start, end+1):
        blocks[i] += 1

max_block = 0
for block in blocks:
    if max_block < block:
        max_block = block
        
print(max_block)

