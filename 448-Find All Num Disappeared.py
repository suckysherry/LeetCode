def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0]*len(nums)
        result = []
        
        for num in nums:
            count[num-1] += 1
        
        for i in range(len(count)):
            if count[i] == 0:
                result.append(i+1)
        
        return result

if __name__ == '__main__':
    nums2 = [1,3,4,3]

    results = findDisappearedNumbers(nums2)
    print results