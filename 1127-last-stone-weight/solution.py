class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            a_stone = stones.pop()
            b_stone = stones.pop()
            diff_stone = a_stone - b_stone

            if diff_stone and stones:
                if stones[-1] <= diff_stone:
                    stones.append(diff_stone)       
                else:
                    for idx, stone in enumerate(stones):
                        if stone >= diff_stone:
                            stones.insert(idx, diff_stone)
                            break

        if not stones and diff_stone:
            return diff_stone

        return stones[0] if stones else 0
