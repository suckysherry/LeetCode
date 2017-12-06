def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        nums.sort()
        
        total = 0
        for i in nums[::2]:
            total += i
        return total

if __name__ == '__main__':
    nums = [0,0,1]
    results = moveZeroes(nums)
    print results