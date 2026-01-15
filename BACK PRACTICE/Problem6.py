def longest_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n          # dp[i] = length of LIS ending at i
    prev = [-1] * n       # prev[i] = previous index in the subsequence

    max_len = 1
    max_index = 0

    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i

    # Reconstruct the subsequence
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]

    return lis[::-1]


# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums)) 
