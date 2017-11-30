def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

if __name__ == '__main__':
    List = [2,4]
    List1 =[1,2,3,4]
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

    results = nextGreaterElement(nums1, nums2)
    print results
