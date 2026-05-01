import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sum_target = sum(target)
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)

        while True:
            curr_val = - heapq.heappop(max_heap)
            if curr_val == 1:
                return True
                
            sum_others = sum_target - curr_val
            if sum_others == 1:
                return True
            elif sum_others < 1 or curr_val <= sum_others:
                return False

            next_val = curr_val % sum_others
            if next_val == 0:
                return False
                
            heapq.heappush(max_heap, - next_val)
            sum_target -= curr_val - next_val




