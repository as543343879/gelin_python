#
# 136. 只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
from functools import reduce
from typing import List


class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        dict_info = {}
        for key in nums:
            dict_info[key] = int(dict_info.get(key, 0)) + 1

        for key in dict_info.keys():
            if dict_info[key] == 1:
                return key

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

s = Solution()
res = s.singleNumber([1, 2, 2])
print(res)
