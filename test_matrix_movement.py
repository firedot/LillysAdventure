matrix = [[' ' for _ in range(5)] for _ in range(5)]

current_pos = [0, 0]

def step(direction, pos, mat, val):
   #Crude but working.
   if direction == 'up':
    new_pos = pos[0] - val
    if new_pos > 0 and new_pos <= (len(mat) - 1):
        print(f'values on the new row (x) are: {matrix[new_pos]}')
        pos[0] = new_pos
    else: 
       print('you are on the border of the matrix')
   elif direction == 'down':
       new_pos = pos[0] + val
       if new_pos <= (len(mat) - 1):
           print(f'values on the new row (x) are: {matrix[new_pos]}')
           pos[0] = new_pos
       else: 
           print('you are on the border of the matrix') 
   elif direction == 'left':
       new_pos = pos[1] - val
       if 0 <= new_pos <= (len(mat[pos[0]]) - 1): 
          print(f'values on the new row (x) are: {matrix[pos[0]][new_pos]}')
          pos[1] = new_pos
       else: 
           print('you are on the border of the matrix') 
   elif direction == 'right':
       new_pos = pos[1] + val
       if 0 >= new_pos  <= (len(mat[pos[0]]) - 1): 
          print(f'values on the new row (x) are: {matrix[pos[0]][new_pos]}')
          pos[1] = new_pos
       else: 
           print('you are on the border of the matrix') 
        
        
#print(matrix)

#for i in range(len(matrix)):
#   print(matrix[i])

for i in range(len(matrix)):
   print(matrix[2][i])
   
#print(matrix[-1])

step('down', current_pos, matrix, 1)
step('down', current_pos, matrix, 3)
step('left', current_pos, matrix, 3)
step('right', current_pos, matrix, 2)
print(len(matrix[0]))
print(current_pos)
    

