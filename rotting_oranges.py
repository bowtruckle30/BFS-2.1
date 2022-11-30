class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = []
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1
        time = 0
        
        while queue and fresh>0:
            
            for i in range(len(queue)):
                x, y = queue.pop(0)
                
                for p, q in dirs:
                    if x + p in range(ROWS) and y + q in range(COLS) and grid[x + p][y + q] == 1:
                        grid[x + p][y + q] = 2
                        fresh -= 1
                        queue.append([x + p, y + q])
            time += 1
        
        return time if fresh == 0 else -1
        