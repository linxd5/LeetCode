class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result, temp_list = [0], [0]

        for i in range(1, num+1):
            if len(temp_list) == 0:
                temp_list = result[:] 
            result.append(temp_list.pop(0)+1)

        return result

temp = Solution()
print temp.countBits(20)
