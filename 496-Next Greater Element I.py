def nextGreaterElement(findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = []
        for item in findNums:
            flag = 0
            for j in range(len(nums)):
                if nums[j] == item:
                    flag = 1
                if flag == 1:
                    if nums[j] > item:
                        rlist.append(nums[j])
                        break
                if j == (len(nums)-1) and flag == 1:
                    rlist.append(-1)
                    break
        return rlist

if __name__ == '__main__':
    List = [2,4]
    List1 =[1,2,3,4]
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

    results = nextGreaterElement(nums1, nums2)
    print results
