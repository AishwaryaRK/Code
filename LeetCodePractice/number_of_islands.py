visited={}
def get_number_of_islands(binaryMatrix):
  r = len(binaryMatrix)
  c = len(binaryMatrix[0])
  number_of_islands = 0
  for i in range(0, r):
    for j in range(0, c):
      key = str(i)+","+str(j)
      if key not in visited and binaryMatrix[i][j] == 1:
          mark_island_cells(i,j,binaryMatrix)
          number_of_islands += 1
  return number_of_islands

def mark_island_cells(i,j,binaryMatrix):
  stack = [(i,j)]
  while len(stack) != 0:
    e = stack.pop()
    r = e[0]
    c = e[1]
    key = str(r)+","+str(c)
    if key not in visited:
      visited[key] = 1
      if r+1 < len(binaryMatrix) and binaryMatrix[r+1][c]==1:
        stack.append((r+1,c))
      if r-1 >= 0 and binaryMatrix[r-1][c]==1:
        stack.append((r-1,c))
      if c+1 < len(binaryMatrix[0]) and binaryMatrix[r][c+1]==1:
        stack.append((r,c+1))
      if c-1 >= 0 and binaryMatrix[r][c-1]==1:
        stack.append((r,c-1))

mat = [[1,0,1,0]]
print(get_number_of_islands(mat))