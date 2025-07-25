n = int(input())
nums = list(map(int, input().split()))

nums = list(sorted(nums))
for elem in nums:
    print(elem, end=' ')
print()

nums = nums[::-1]
for elem in nums:
    print(elem, end=' ')