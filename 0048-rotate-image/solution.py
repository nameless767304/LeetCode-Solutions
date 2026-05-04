class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        val_x = n // 2 + 1 if n % 2 else n // 2
        val_y = n // 2

        n -= 1
        for y in range(val_y):
            for x in range(val_x):
                point1 = (y, x)
                point2 = (point1[1], n - point1[0])
                point3 = (point2[1], n - point2[0])
                point4 = (point3[1], n - point3[0])
                # print(point1)
                # print(point2)
                # print(point3)
                # print(point4)

                matrix[point1[0]][point1[1]], matrix[point2[0]][point2[1]], matrix[point3[0]][point3[1]], matrix[point4[0]][point4[1]] = matrix[point4[0]][point4[1]], matrix[point1[0]][point1[1]], matrix[point2[0]][point2[1]], matrix[point3[0]][point3[1]]
                


# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# 30 20 10 00
# 31 21 11 01
# 32 22 12 02
# 33 23 13 03

# Ax, Ay
# Bx, By

# By = Ax
# Bx = n - Ay

# Ax = By
# Ay = n - Bx
# Bx = n - Ay
# By = Ax

# x, y


# 3x3 -> 2 + 1
# 4x4 -> 4
# 5x5 -> 6 + 1
# 6x6 -> 9
# 7x7 -> 12 + 1

# 1x2
# 2x2
# 2x3
# 3x3
# 3x4





