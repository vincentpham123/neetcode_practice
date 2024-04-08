import collections
def closest_carrot(grid, starting_row, starting_col):
  visited = set([(starting_row, starting_col)])
  # i want to implement BFS

  q = collections.deque([ (starting_row, starting_col, 0)])


  while q:
    row, col, distance = q.popleft()

    if grid[row][col] == 'C':
      return distance 
    # return distance if it is a carrot 

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for delta in deltas:
      delta_row, delta_col = delta 
      neighbor_row , neighbor_col = delta_row + row, delta_col + col 

      pos = (neighbor_row, neighbor_col)
      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <=  neighbor_col < len(grid[0])

      if row_inbounds and col_inbounds and pos not in visited and grid[neighbor_row][neighbor_col] !='X':
        visited.add(pos)
        q.append((neighbor_row, neighbor_col, distance + 1))
  return -1

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
                # if its in old to new, there is alread a clone 
            copy = Node(node.val)

            oldtonew[node] = copy 

            # now to check the neighbors 
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                #this will return a copy 

            return copy
        return dfs(node) if node else None
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # this is a graph problem
        # ill be traversing through a grid, searching for connecting 1's

        visited = set()

        max_area = float('-inf')
        
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):

            # water '0', out of bounds, and visited 

            if (
                r not in range(rows)
                or c not in range(cols)
                or (r,c) in visited
                or grid[r][c] == 0
            ):
                # checking for visited because if we visited, that means we dont need to count it again 
                return 0 
            
            visited.add((r,c))

            left = dfs(r-1,c)
            right = dfs(r+1,c)
            up = dfs(r, c+1)
            down = dfs(r, c-1)

            # those will all be returning integers

            return 1 + left + right + up + down 
        
        for r in range(rows):
            for c in range(cols):
                island_count = dfs(r, c)
                max_area = max(island_count, max_area)
        
        if max_area == float('-inf'):
            return 0
        else:
            return max_area
        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific grid[r][0], grid[0][c]
        # atlantic grid[-1][c], grid[r][-1]

        # find the 

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        # check the height of a grid, then check north, west, south, east 
        # we hit 
        # for pacific: we keep going until we hit c = 0 , r=0
        # for atlantic : we keep going until we hit r = len(grid) - 1. c = len(grid[0])-1 
        # if it hits both then true and we add to the results 
        # we add everything to visited 

        # base case:
        # if the grid[r][c] > the current height, so i need to store the current value in the dfs 

        def dfs(r, c, visited, height):
            if (
                (r, c) in visited
                or r < 0 
                or c < 0 
                or r == rows
                or c == cols
                or heights[r][c] < height
            ):
                return 
            
            visited.add((r,c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c,visited,  heights[r][c])
            dfs(r, c+1,visited,  heights[r][c])
            dfs(r, c-1,visited, heights[r][c])
        
        for c in range(cols):
            dfs(0,c,pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        #going out from the edge inwards, 
        # instead of branching out
        # we are going from the top and bottom row which are atlantic and pacific
        # and running out DFS until it reaches an edge 

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        res = []
        for r in range(rows):
            for c in range(cols):
                pair = (r,c)
                if pair in pac and pair in atl:
                    res.append([r,c])
        
        return res

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # i know any island with connected to an edge will never become X's
        # so i just need to find those and mark them 

        # once i mark them, i can do another for loop, and chagne an O's that were not marked

        def dfs(r,c):
            if (
                r<0
                or c < 0
                or r == rows
                or c == cols
                or board[r][c]!='O'
            ):
                return 
            
            board[r][c] = 'T'
            #marking the islands on the edge 

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        # so we'll call this on on the surrounding areas of the grid 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0,rows-1] or c in [0,cols-1]):
                    # limiting the calls to islands on the edge
                    dfs(r, c)
                
        # now that all surrounded islands are marked, we can go and change the remaining Os to X's

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c] = 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='T':
                    board[r][c] = 'O'
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        time = 0
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                # check for fresh and rottens
                # rottens we append to queue, 
                # fresh we add tot he fresh count 

                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[1,0],[-1,0], [0,1], [0,-1]]
        while fresh > 0 and q:
            
            # i need to pop everything in the queue
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (
                        row >=0
                        and col >= 0
                        and row < rows
                        and col < cols
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1 
            time += 1
        
        return time if fresh==0 else -1
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])

        pac, atl = set(), set()
        # the idea is that we will dfs from positions only on the borders
        # if a position is in both sets, that means that it can be used to traverse to both oceans


        def dfs(r, c, height,visited):

            if (
                (r,c) in visited
                or r < 0 
                or c < 0
                or r == rows
                or c == cols
                or heights[r][c] < height
                # we are checing this because the next position needs to be greater as we are going backwards
            ):
                return 
            
            visited.add((r,c))

            dfs(r+1,c, heights[r][c], visited )
            dfs(r-1,c, heights[r][c], visited )
            dfs(r,c+1, heights[r][c], visited )
            dfs(r,c-1, heights[r][c], visited )
        

        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            # i know that this will only check the the first row of the grid 
            dfs(rows-1, c, heights[rows-1][c], atl)
            # i know that this will only the last row of the grid ( atlantic ocean)
        

        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols-1, heights[r][cols-1], atl)
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # i will need to chagne fresh oranges to rotten
        
        # i think the best way to approach this problem is through DFS
        # DFS will allow me to keep track of the spoiling process just by its nature 

        q = collections.deque()


        rows, cols = len(grid), len(grid[0])

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # i know if its rotten, i need to append to the q
                    q.append((r,c))
                if grid[r][c] == 1:
                    # what if i find a fresh 
                    # this will be used to detemrine the result
                    # as i spoil an orange, I'll decrement the fresh
                    fresh += 1
        
        time = 0 

        directions = [[1,0], [-1,0],[0,1],[0,-1]]
        while fresh > 0 and q :

            length = len(q)
            # this is so I only pop the most recently added cordinates 

            for i in range(length):
                row, col = q.popleft()
                # assuming this is the first rotten orange
                # i need to traverse the graph

                for dr, dc in directions:
                    new_row, new_col = row + dr, col+dc 

                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and grid[new_row][new_col]==1
                    ):
                        # what do i do if its fresh
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh -= 1 
            time += 1

        return time if fresh == 0 else -1
                        