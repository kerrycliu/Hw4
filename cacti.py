'''You’re planting cacti in a popular video game in a square or rectangular area. Some blocks have cacti, while
others do not. Cacti cannot be placed adjacent to each other (horizontally or vertically), but CAN be placed
diagonal to each other.
You have a 2-D Array that shows which blocks you’ve already planted cacti on, with 0 meaning an empty
plot, and 1 meaning a used plot. How many more cacti can you plant on this plot before it’s full?
Instructions:
• Create a file named cacti.py and create a decorator inside called cacti_number.
• The function will take a 2-D array as input.
• The function should return an integer.
• Your function can assume that each index of the array will only use 0 or 1, and will be a perfect
rectangle or square (each subarray has the same length). Your function can also assume that two cacti
aren’t already next to each other.'''


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


