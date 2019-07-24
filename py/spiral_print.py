import unittest
"""
Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
    1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

"""


def get_spiral(matrix):
    assert len(matrix), "{}: not a valid matrix".format(matrix)
    # 1-d array, no need to do spiral walk
    if not isinstance(matrix[0], list):
        return matrix

    row_end = len(matrix)
    col_end = len(matrix[0])
    row_start = 0
    col_start = 0

    for entry in matrix:
        assert len(entry) == col_end, "Matrix should be symetrical"

    spiral = []
    total_ele = row_end * col_end
    # len(spiral) == total_ele is required to handle rectangular matrix
    # this check will ensure we walked through all the elements and will
    # not to redo on elements that were already covered
    while row_end > row_start and col_end > col_start:
        # traverse towards right (1st row, each column)
        for i in range(col_start, col_end):
            if len(spiral) == total_ele:
                break
            spiral.append(matrix[row_start][i])
        # mark 1st row as complete
        row_start += 1

        # traverse downwards (each row, last column)
        for i in range(row_start, row_end):
            if len(spiral) == total_ele:
                break
            spiral.append(matrix[i][col_end - 1])
        # mark the last column as complete
        col_end -= 1

        # traverse towards left (last row, each column)
        for i in range(col_end - 1, col_start - 1, -1):
            if len(spiral) == total_ele:
                break
            spiral.append(matrix[row_end - 1][i])
        # mark the last row as complete
        row_end -= 1

        # tarverse upwards (each row, first column)
        for i in range(row_end - 1, row_start  - 1, -1):
            if len(spiral) == total_ele:
                break
            spiral.append(matrix[i][col_start])
        # mark the first column as complete
        col_start += 1

    return spiral


class TestSpiralPrint(unittest.TestCase):

    def check_spiral_walk(self, matrix, exp_output):
        spiral_output = get_spiral(matrix)
        print "\n"

        print "Input:     ", matrix
        print "Expected:  ", exp_output
        print "Generated: ", spiral_output

        self.assertEquals(exp_output, spiral_output)
        print "PASS"

    def test_1(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        exp_output = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.check_spiral_walk(matrix, exp_output)

    def test_2(self):
        matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
        exp_output = [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
        self.check_spiral_walk(matrix, exp_output)

    def test_invalid_input_1d_matrix(self):
        matrix = [1, 2, 3, 4]
        exp_output = matrix
        self.check_spiral_walk(matrix, exp_output)

    def test_empty_1d_matrix(self):
        matrix = []
        try:
            get_spiral(matrix)
        except AssertionError as e:
            print e
        else:
            raise AssertionError("code accepting in valid input")

    def test_empty_empty_matrix(self):
        matrix = [[]]
        exp_output = []
        self.check_spiral_walk(matrix, exp_output)


if __name__ == '__main__':
    unittest.main()
