import bisect

def longest_increasing_subsequence(nums):
    if not nums:
        return []

    tails = []           # holds the smallest tail of all increasing subsequences
    size = 0
    parent = [-1] * len(nums)
    index_at_length = [0] * len(nums)

    for i, num in enumerate(nums):
        pos = bisect.bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

        index_at_length[pos] = i
        if pos > 0:
            parent[i] = index_at_length[pos - 1]

        size = max(size, pos + 1)

    # Reconstruct subsequence
    lis = []
    k = index_at_length[size - 1]
    while k != -1:
        lis.append(nums[k])
        k = parent[k]

    return lis[::-1]


# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums))
