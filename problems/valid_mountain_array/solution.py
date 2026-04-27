class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        
        judge = "increase"     
        for idx in range(len(arr) - 1):
            if judge == "increase":
                if arr[idx] < arr[idx + 1]:
                    continue
                elif arr[idx] == arr[idx + 1]:
                    return False
                else:
                    if idx == 0:
                        return False
                    judge = "decrease"
                    
            else:
                if arr[idx] > arr[idx + 1]:
                    continue
                else:
                    return False
                    
        return True if judge == "decrease" else False
            