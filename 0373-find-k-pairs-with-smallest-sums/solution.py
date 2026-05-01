import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        min_heap = []
        length2 = len(nums2)
        length_ans = 0

        for idx in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[idx] + nums2[0], idx, 0))

        while min_heap and length_ans < k:
            curr, idx1, idx2 = heapq.heappop(min_heap)
            ans.append([nums1[idx1], nums2[idx2]])
            length_ans += 1

            if idx2 + 1 < length2:
                heapq.heappush(min_heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))


        return ans
