def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums[::-1]:
            if i == 0:
                count += 1
                nums.remove(i)
        nums = nums.extend([0]*count)
        return nums

if __name__ == '__main__':
    nums = [0,0,1]
    results = moveZeroes(nums)
    print results