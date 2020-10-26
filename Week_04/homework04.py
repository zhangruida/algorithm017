
860.柠檬水找零
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i=j=0
        for k in bills:
            if k==5:i+=1
            elif k==10:j+=1;i-=1
            else:
                if j==0:i-=3
                else:i-=1;j-=1
            if i<0 or j<0:return False
        return True

122.买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i] - prices[i-1]    for i in range(1,len(prices))  if prices[i] - prices[i-1]>0)



455. 分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        kid = 0
        i = 0
        for a in s:
            if i == len(g):
                break
            if g[i] <= a:
                 kid += 1
                 i += 1
        return kid


127.单词接龙
class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0

200.岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':  # 发现陆地
                    count += 1  # 结果加1
                    grid[row][col] = '0'  # 将其转为 ‘0’ 代表已经访问过
                    # 对发现的陆地进行扩张即执行 BFS，将与其相邻的陆地都标记为已访问
                    # 下面还是经典的 BFS 模板
                    land_positions = collections.deque()
                    land_positions.append([row, col])
                    while len(land_positions) > 0:
                        x, y = land_positions.popleft()
                        for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:  # 进行四个方向的扩张
                            # 判断有效性
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'  # 因为可由 BFS 访问到，代表同属一块岛，将其置 ‘0’ 代表已访问过
                                land_positions.append([new_x, new_y])
        return count
