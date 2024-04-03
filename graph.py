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