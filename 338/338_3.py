#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result, temp_list = [0], [0]
        num1, num2 = 1, 0

        for i in range(1, num+1):
            result.append(result[num2]+1)
            num2 += 1
            if num2 == num1:
                num1 *= 2
                num2 = 0

        return result

temp = Solution()
print temp.countBits(20)


