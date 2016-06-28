class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dl = []
        d = x % 10
        while d:
            dl.append(d)
            x /= 10
            d = x % 10
        print dl
        i = 0
        j = len(dl)-1
        print j
        while i <= j:
            if dl[i] <> dl[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print Solution().isPalindrome(12345)
    print Solution().isPalindrome(123321)
    print Solution().isPalindrome(12321)