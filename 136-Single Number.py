def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for item in nums:
            if count.get(item, 0) == 0:
                count[item] = 1
            else:
                count[item] += 1

        for i in count.keys():
            if count[i] == 1:
                return i

if __name__ == '__main__':
    List = [2,4]
    List1 =[1,2,3,4]
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

    results = nextGreaterElement(nums1, nums2)
    print results
