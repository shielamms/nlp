import numpy as np

def get_levenshtein_distance(string1, string2):
    matrix = np.zeros((len(string2)+1, len(string1)+1))

    # Initialize the first row
    for col in range(len(matrix[0])):
        matrix[0][col] = col

    # Initialize the first column
    for row in range(len(matrix)):
        matrix[row][0] = row

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if string1[col-1] == string2[row-1]:
                matrix[row][col] = matrix[row-1][col-1]
            else:
                # separate left, diagonal, and top into separate variables
                # just for clarity during demonstrations
                left = matrix[row][col-1]
                diagonal = matrix[row-1][col-1]
                top = matrix[row-1][col]
                minimum = min(left, diagonal, top)
                matrix[row][col] =  minimum + 1

    return matrix[len(matrix)-1][len(matrix[0])-1]
