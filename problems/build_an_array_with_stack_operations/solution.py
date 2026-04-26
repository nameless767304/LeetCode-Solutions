class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        target.reverse()

        for num in range(1, n + 1):
            if not target:
                break

            if target[-1] == num:
                ans.append("Push")
                target.pop()
            else:
                ans.extend(["Push", "Pop"])

        return ans