64. 最小路径和
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

91. 解码方法
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0 
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[-1] += dp[-2]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[-1] += dp[-3]
            dp.pop(0)
        
        return dp[-1]

221. 最大正方形
class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        res = 0  # 记录结果
        # 定义dp数组，每个元素代表当前位置可以达到的最大的正方形的边长
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return pow(res, 2)

621. 任务调度器
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length

647. 回文子串
class Solution:
        def countSubstrings(self, s: str) -> int:
            n = len(s)
            self.res = 0
            def helper(i,j):
                while i >= 0 and j < n and s[i] == s[j]:
                    i -= 1
                    j += 1
                    self.res += 1
            for i in range(n):
                helper(i,i)
                helper(i,i+1)
            return self.res
