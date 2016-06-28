class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = list()
        numIndexMap = dict()

        # iterator nums array to get value->index map
        for i, num in enumerate(nums):
            numIndexMap[num] = i

        for k in numIndexMap:
            diff = target - k
            if diff in numIndexMap:
                # we are done
                ret.append(numIndexMap[k])
                ret.append(numIndexMap[diff])
                break
        return ret


if __name__ == '__main__':
    nums = [2, 11, 7, 15]
    target = 9
    obj = Solution()
    ret = obj.twoSum(nums, target)
    print ret
