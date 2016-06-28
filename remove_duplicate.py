class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if j < len(nums) and nums[j] <> nums[i]:
                i += 1
                nums[i] = nums[j]
                j += 1
        print nums[0:i + 1]
        return i + 1


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7])
