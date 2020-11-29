387. 字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self, s: str) -> int:
        Hash = {}
        for i in s:
            Hash[i] = Hash.get(i, 0) + 1

        for key in Hash.keys():
            if Hash[key] == 1:
                return s.find(key)
        
        return -1


541. 反转字符串 II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, flag = "", True
        for i in range(0, len(s), k):
            res += s[i:i + k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res


151. 翻转字符串里的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回


557. 反转字符串中的单词 III
class Solution(object):
    def reverseWords(self, s):
         return " ".join(s[::-1].split(" ")[::-1])



917. 仅仅反转字母
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        left,right=0,len(S)-1

        while left<right:
            if S[left].isalpha() and S[right].isalpha():
                S[left],S[right] = S[right],S[left]
                left += 1
                right -= 1
            elif not S[left].isalpha() and S[right].isalpha():
                left += 1
            elif S[left].isalpha() and not S[right].isalpha():
                right -= 1
            elif not S[left].isalpha() and not S[right].isalpha():
                left += 1
                right -= 1

        return ''.join(S)


205. 同构字符串
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        dic={}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=t[i]
            else:
                if dic[s[i]]!=t[i]:
                    return False
        return True



680. 验证回文字符串 Ⅱ
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True
