num_arr = list(map(int, input().split()))

num_arr.pop(len(num_arr)-1)

max_num = max(num_arr)
min_num = min(num_arr)
print(f"{max_num} {min_num}")