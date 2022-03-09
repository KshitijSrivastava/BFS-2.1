
#Rotting Oranges
# (https://leetcode.com/problems/rotting-oranges)


class LevelNode:
    def __init__(self, i, j, level):
        self.i = i
        self.j = j
        self.level = level
        

class Solution:
    def isInsideGrid(self, i, j, nrows, ncols):
        return i >= 0 and i < nrows and j >= 0 and j < ncols
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #find number of rows and cols
        nrows = len(grid)
        ncols = len(grid[0])
        
        max_level = 0
        
        #keeps frack of visited nodes
        visited = []
        for i in range(nrows):
            visited.append( [False for j in range(ncols)] )
        
        #inserts the rotten oranges into the queue
        #Also counts the number of rotten and not rotten oranges = orange_count
        queue = []
        orange_count = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    orange_count += 1
                
                if grid[i][j] == 2:
                    queue.append( LevelNode(i, j, 0) )
                    visited[i][j] = True
        
        #while queue is not empty
        count = 0
        while len(queue) != 0:
            #pops the element
            ln = queue.pop(0)
            i = ln.i
            j = ln.j
            level = ln.level
            #counts the number of nodes
            count += 1
            
            #finds the max_level (time)
            max_level = max(max_level, level)
            
            #interate in all directions
            for dx, dy in [ (0, 1), (1,0), (-1, 0), (0, -1) ]:
                new_i = i + dx
                new_j = j + dy
                #if inside the grid and not rotten orange and not visited
                #insert to the queue and make it visited
                if self.isInsideGrid(new_i, new_j, nrows, ncols) and \
                grid[new_i][new_j] == 1 and not visited[new_i][new_j]:
                    queue.append( LevelNode(new_i, new_j, level + 1) )
                    visited[new_i][new_j] = True
                    
        # print("count = ", count)
        # print("orange_count = ", orange_count)

        #compare total_oranges with rotten_count
        if count == orange_count:
            return max_level
        return -1