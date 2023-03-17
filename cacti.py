def cacti_number(func):
    def wrapper(array):
        row = len(array)
        col = len(array[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if array[i][j] == 0:
                    # top
                    # left
                    # bottom
                    # right
                    # top left
                    # bottom left
                    # bottom right
                    # top right
                    if (i == 0 or array[i-1][j] == 0) and \
                        (j == 0 or array[i][j-1] == 0) and\
                        (i == row - 1 or array[i+1][j] == 0) and \
                        (j == col -1 or array[i][j+1] == 0) and \
                        (i == 0 or j == 0 or array[i-1][j-1] == 0) and\
                        (i == row - 1 or j == 0 or array[i+1][j-1] == 0) and\
                        (i == row - 1 or j == col - 1 or array[i+1][j+1] == 0) and\
                        (i == 0 or j == col - 1 or array[i-1][j+1] == 0):
                        count+=1
        return count
    return wrapper


