class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur_row = 0
        step = 1

        for c in s:
            rows[cur_row] += c
            cur_row += step

            if cur_row == 0 or cur_row == numRows - 1:
                step = -step

        return ''.join(rows)