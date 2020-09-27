两道题
1. 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

2.加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newlist = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlist.append(0)
        if not digits:
            return [1] + newlist
        else:
            digits[-1] += 1
            return digits + newlist
