# 回文串
# https://leetcode-cn.com/problems/valid-palindrome/
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
#
#
# 示例
# 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama"
# 是回文串
class Solution:

    def isPalindrome(self, s: str) -> bool:
        s_len = len(s)
        if s_len == 1:
            return True
        start = 0
        end = s_len - 1

        while start < end:
            if s[start].isalnum() is False:
                start += 1
                while s[start].isalnum() is False and start < end:
                    start += 1

            if s[end].isalnum() is False:
                end -= 1
                while s[end].isalnum() is False and end > start:
                    end -= 1

            if start > end:
                return True

            if s[start].lower() != s[end].lower():
                print( s[start], s[end])
                return False
            start += 1
            end -= 1

        return True



t = Solution()
# print(t.isPalindrome("A man, a plan, a canal: Panama"))
print(t.isPalindrome(".,"))
print("a".isalnum())