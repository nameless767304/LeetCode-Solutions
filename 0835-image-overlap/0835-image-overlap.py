class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_1 = []
        img2_1 = []
        n = len(img1)
        vector = {}

        for row in range(n):
            for col in range(n):
                if img1[row][col]:
                    img1_1.append((row, col))
                if img2[row][col]:
                    img2_1.append((row, col))

        for loc_1 in img1_1:
            for loc_2 in img2_1:
                v = (loc_1[0] - loc_2[0], loc_1[1] - loc_2[1])
                vector[v] = vector.get(v, 0) + 1

        ans = 0
        for count in vector.values():
            ans = max(ans, count)

        return ans

