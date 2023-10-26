def getGridInd(row_no, column_no, grid, width):
    """
    This function returns the index of the element in the list corresponding
    to the grid location represented by the row_no and column_no.
    inputs:
    row_no		: The row number (numbers starts from 0). [integer]
    column_no	: The column number (numbers starts from 0). [integer]
    grid 		: The list containing the information about the grid [integer]
    width 		: Width of the grid. This can be used to calculate the number of rows. [integer]
    
    returns: This function returns the index [integer]
    
    For more details check the Assignment 5 document.
    
    """
    # Write your code here
    
    if row_no >= len(grid) // width or column_no > width:
        
        return -1
    
    else:
        
        ind = row_no * width + column_no
    
    return ind

    pass


def checkNextStep(curr_pos, dir, grid, width):
    """
    This function checks whether the robot can take the next step in the direction given by
    dir argument.
    
    inputs:
    curr_pos	: This contains the position of the robot. First element of the list gives
                the row number and the second element give the column number. [list]
    dir 		: Direction of the next move ‘N’ for north, ‘E’ for East, ‘S’ for South, and ‘W’ for west.
    grid 		: The list containing the information about the grid [integer]
    width 		: Width of the grid. This can be used to calculate the number of rows. [integer]
    
    returns: A string
    'invalid'	: Current position is outside of the grid or on an obstacle.
    'go' 		: Next position is free.
    'obstacle'	: Next position has an obstacle
    'out of bound': Next position is out of bound.
    'Hooray' 	: Next position is goal
    
    For more details check Assignment 5 document.
    """
    # Write your code here
    
    pos = getGridInd(curr_pos[0],curr_pos[1],grid,width)
    
    if pos == -1 or grid[pos] == 'O':
        
        return 'invalid'
    
    else:
        
        next_pos = 0
        
        if dir == 'N':
            
           next_pos = pos - width
            
        if dir == 'S':
            
           next_pos = pos + width
            
        if dir == 'E':
            
            next_pos = pos + 1
            
        if dir == 'W':
            
           next_pos = pos - 1
        
        
        if 0 < next_pos < len(grid):
            
            if grid[next_pos] == 'F':
                
                return 'go'
                
            if grid[next_pos] == 'O':
                
                return 'obstacle'
                
            if grid[next_pos] == 'G':
                
                return 'Hooray'
            
        else:
            
            return 'out of bound'
        
    pass


if __name__ == '__main__':
    """
    This example refers to the grid given in the assignment.
    However, your implementation should be able to handle a grid of any size
    grid = ['F', 'F', 'F', 'F', 'F', 'F', 'O', 'F', 'F', 'F',\
            'F', 'F', 'O', 'F', 'F', 'O', 'F', 'O', 'F', 'F',\
            'F', 'O', 'O', 'F', 'F', 'F', 'F', 'F', 'O', 'F',\
            'F', 'F', 'F', 'O', 'O', 'O', 'O', 'F', 'O', 'F',\
            'F', 'O', 'F', 'F', 'F', 'F', 'G', 'F', 'F', 'F']
    
    Width of this grid (Number of columns) is 10.
    """
    # Write your test code here
    grid = ['F', 'F', 'F', 'F', 'F', 'F', 'O', 'F', 'F', 'F',\
            'F', 'F', 'O', 'F', 'F', 'O', 'F', 'O', 'F', 'F',\
            'F', 'O', 'O', 'F', 'F', 'F', 'F', 'F', 'O', 'F',\
            'F', 'F', 'F', 'O', 'O', 'O', 'O', 'F', 'O', 'F',\
            'F', 'O', 'F', 'F', 'F', 'F', 'G', 'F', 'F', 'F']
    width = 10