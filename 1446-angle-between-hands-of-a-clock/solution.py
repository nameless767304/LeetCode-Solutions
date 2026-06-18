class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12

        short = 30 * hour + 0.5 * minutes
        long = 6 * minutes

        diff = abs(short - long)

        if diff > 180:
            return 360 - diff
        else:
            return diff
