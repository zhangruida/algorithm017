77.组合

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
         return list(itertools.combinations(range(1,n+1),k))



46.全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


47.全排列 II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 数组先排序
        self.res = []
        self.recur(nums,[])
        return self.res

    def recur(self,nums,temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                continue
            self.recur(nums[:i]+nums[i+1:],temp+[nums[i]]) #nums[:i]+nums[i+1:] 避免了重复利用。


236. 二叉树的最近公共祖先
class Solution: 
def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
 if not root or root == p or root == q: return root
left = self.lowestCommonAncestor(root.left, p, q) 
right = self.lowestCommonAncestor(root.right, p, q) 
if not left and not right: return
if not left: return right 
if not right: return left 
return root

105. 从前序与中序遍历序列构造二叉树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i+1:])

        return root
