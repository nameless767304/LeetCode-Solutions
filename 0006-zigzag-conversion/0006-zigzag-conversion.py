class Solution:
    def convert(self, s: str, numRows: int) -> str:
        Rows = {row: [] for row in range(numRows)}
        interval = 0 if numRows == 1 else numRows * 2 - 3
        ans = []

        for row in range(numRows):
            idx = row
            while idx < len(s):
                Rows[row].append(s[idx])
                if row > 0 and row < numRows - 1:
                    if idx + (interval + 1 - 2 * row) < len(s):
                        Rows[row].append(s[idx + (interval + 1 - 2 * row)])
                idx += interval + 1
            
        for row in Rows.values():
            ans.extend(row)

        return "".join(ans)