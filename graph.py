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