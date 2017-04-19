"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6
"""

def differentSquares(matrix):
    w=len(matrix[0])
    h=len(matrix)
    if w<2 or h<2:
        return 0
    quads=[]
    for r in range(h-1):
        row=[]
        for c in range(w-1):
            q=[matrix[r][c],matrix[r][c+1],matrix[r+1][c],matrix[r+1][c+1]]
            row.append(q)
        for thing in row:
            quads.append(thing)
    #print(quads)
    seen=[quads[0]]
    for item in quads[1:]:
        if item not in seen:
            seen.append(item)
    #print(seen)
    return len(seen)