class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        
        last_list, current_list, next_list = [1], [0, 1], []
        for i in range(1, num+1):
            if len(next_list) == 0:
                next_list = last_list[:] + [x+1 for x in last_list]
                last_list = next_list[:]
            current_list.append(next_list.pop(0))
        return current_list


temp = Solution()
print temp.countBits(20)
