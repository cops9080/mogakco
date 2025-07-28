n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums = list(sorted(nums))

print(nums[k-1])
