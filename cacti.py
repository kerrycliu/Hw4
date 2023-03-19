def cacti_number(array):
    count = 0
    row = len(array)
    col = len(array[0])
   #check if only 1 row, nultiple column
    if row == 1 and col > 1:
        for j in range(col):
            if array[0][j] == 0:
                #check corners:
                if j == 0 or j == col - 1:
                    if (j == 0 and array[0][j+1] == 0) or (j == col-1 and array[0][j-1] == 0):
                        array[0][j] = 1
                        count += 1
                else: #somewhere in the middle
                    if array[0][j+1] == 0 and array[0][j-1] == 0:
                        array[0][j] = 1
                        count += 1
    # check if only one column, multiple rows
    elif row > 1 and col == 1:
        for i in range(row):
            if array[i][0] == 0:
            # check top and bottom is 0
                if i == 0 or i == row - 1:
                    if (i == 0 and array[i+1][0] == 0) or (i == row - 1 and array[i-1][0] == 0):
                        array[i][0] = 1
                        count += 1
                else:
                    if array[i+1][0] == 0 and array[i-1][0] == 0:
                        array[i][0] = 1
                        count += 1
    elif row > 1 and col > 1: #more than 1 row / 1 column
        for i in range(row):
            for j in range(col):  
                if array[i][j] == 0:
                    #if i == 0 or j == 0 or i == row-1 or j == col-1: # in the corner
                    #top left corner
                    if i == 0 and j == 0: 
                        #checking right and bottom
                        if array[i][j+1] == 0 and array[i+1][j] == 0:
                            array[i][j] = 1
                            count += 1
                    #top right corner
                    elif i == 0 and j == col-1:   
                        #checking left and bottom                     
                        if array[i][j-1] == 0 and array[i+1][j] == 0:
                            array[i][j] = 1
                            count += 1
                    #bottom left
                    elif i == row-1 and j == 0:
                        #check right and top
                        if array[i][j+1] == 0 and array[i-1][j] == 0:
                            array[i][j] = 1
                            count += 1
                    #bottom right
                    elif i == row-1 and j == col-1:
                        #check left top
                        if array[i][j-1] == 0 and array[i-1][j] == 0:
                            array[i][j] = 1
                            count += 1
                    #top not corners
                    elif i  == 0 and (j != 0 or j != col - 1):
                        if array[i][j-1] == 0 and array[i][j+1] == 0 and array[i+1][j] == 0:
                            array[i][j] = 1
                            count += 1
                    # bottom not corner
                    elif i  == row - 1 and (j != 0 or j != col - 1):
                        if array[i][j-1] == 0 and array[i][j+1] == 0 and array[i-1][j] == 0:
                            array[i][j] = 1
                            count += 1
                    #left not corner
                    elif j == 0 and (i != 0 or i != row - 1):
                        if array[i-1][j] == 0 and array[i+1][j] == 0 and array[i][j+1] == 0:
                            array[i][j] = 1
                            count += 1
                    #right not corner
                    elif j == col - 1 and (i != 0 or i != row - 1):
                        if array[i-1][j] == 0 and array[i+1][j] == 0 and array[i][j-1] == 0:
                            array[i][j] = 1
                            count += 1
                    else:
                        if array[i+1][j] == 0 and array[i-1][j] == 0 and array[i][j+1] == 0 and array[i][j-1] == 0:
                            array[i][j] = 1
                            count += 1

    else:
        if array[0][0] == 0:
            count += 1

    return count



