class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.arr = arr
        self.visited = [False] * len(arr)
        self.length = len(arr)

        return self.nextIndex(start)

    def nextIndex(self, curr) -> bool:
        if curr < 0 or curr >= self.length or self.visited[curr]:
            return False

        if self.arr[curr] == 0:
            return True

        self.visited[curr] = True
        val = self.arr[curr]

        return self.nextIndex(curr - val) or self.nextIndex(curr + val)
