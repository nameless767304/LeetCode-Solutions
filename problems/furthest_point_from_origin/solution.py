class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        point_location = 0
        more_movement = 0

        for move in moves:
            if move == "L":
                point_location -= 1
            elif move == "R":
                point_location += 1
            else:
                more_movement += 1

        return abs(point_location) + more_movement
        
        




