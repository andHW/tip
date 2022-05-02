# https://leetcode.com/contest/biweekly-contest-77/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = []
        for _ in range(m):
            grid.append(['X']*n)

        for w in walls:
            r,c = w
            grid[r][c] = 'W'
        
        # for row in grid:
        #     print(row)
        
        for g in guards:
            r,c = g
            # print(r,c)
            grid[r][c] = 'G'

#         for row in grid:
#             print(row)
        
#         print("---------")

        for g in guards:
            r,c = g
            # up
            for i in range(r-1, -1, -1):
                if grid[i][c] in ['W', 'G']:
                    break
                grid[i][c] = '.'
            # down
            for i in range(r+1, m):
                if grid[i][c] in ['W', 'G']:
                    break
                grid[i][c] = '.'
            # left
            for i in range(c-1, -1, -1):
                if grid[r][i] in ['W', 'G']:
                    break
                grid[r][i] = '.'
            # right
            for i in range(c+1, n):
                if grid[r][i] in ['W', 'G']:
                    break
                grid[r][i] = '.'
        
        # for row in grid:
        #     print(row)

        ans = sum(row.count('X') for row in grid)
        return ans
