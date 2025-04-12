class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n
        cnt = [1] * n
        maxi = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:  
                        cnt[i] += cnt[j]
            maxi = max(dp[i], maxi)
        
        res = sum(cnt[i] for i in range(n) if dp[i] == maxi)
        return res