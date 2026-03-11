class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def check(x):
            operations = 0
            
            for balls in nums:
                operations += (balls - 1) // x
            
            return operations <= maxOperations
        
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left