class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)] 

        for idx_row, submatrix in enumerate(matrix):
            for idx_col, num in enumerate(submatrix):
                # left_region = self.prefix_matrix[idx_row + 1][idx_col]
                # upper_region = self.prefix_matrix[idx_row][idx_col + 1]
                # overlapped_region = self.prefix_matrix[idx_row][idx_col]
                # self.prefix_matrix[idx_row + 1][idx_col + 1] = num + left_region + upper_region - overlapped_region

                self.prefix_matrix[idx_row + 1][idx_col + 1] = num + self.prefix_matrix[idx_row + 1][idx_col] + self.prefix_matrix[idx_row][idx_col + 1] - self.prefix_matrix[idx_row][idx_col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # whole_region = self.prefix_matrix[row2 + 1][col2 + 1]
        # left_region = self.prefix_matrix[row2 + 1][col1]
        # upper_region = self.prefix_matrix[row1][col2 + 1]
        # overlapped_region = self.prefix_matrix[row1][col1]

        # return whole_region - left_region - upper_region + overlapped_region
        
        return self.prefix_matrix[row2 + 1][col2 + 1] - self.prefix_matrix[row2 + 1][col1] - self.prefix_matrix[row1][col2 + 1] + self.prefix_matrix[row1][col1]


