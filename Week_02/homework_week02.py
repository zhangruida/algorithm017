49. 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())


1. 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


144. 二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return 
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res



94. 二叉树的中序遍历              
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		def inorder(root):
			if not root:
				return
			inorder(root.left)
			# 递归完左子树后，处理节点值
			ans.append(root.val)  
			inorder(root.right)
		ans = []
		inorder(root)
		return ans



429. N叉树的层序遍历
class Solution:
	def levelOrder(self, root: 'Node') -> List[List[int]]:
		if not root: return []  # 首先判断root是否有内容，如果没有则输出[]
		queue = [root]  #设置列表queue,前者存放节点
		res = []    #设置res，存放值
		while queue:
			res.append(node.val for node in queue)  #开始循环，通过for循环将queue里面的值分离出来一次性加入res中
            queue = [child for node in queue for child in node.children]    #queue队列通过两个for循环，前面一个取出queue的节点，后一个将取出的节点再取子节点，然后得到queue 
		return res  #最后循环结束输出res



264. 丑数
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
