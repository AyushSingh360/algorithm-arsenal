class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Normalize hour = 12 to 0 for easier math
        hour %= 12
        
        # Each hour = 30 degrees, plus 0.5 degrees per minute
        hour_angle = 30 * hour + 0.5 * minutes  # [web:5][web:7]
        
        # Each minute = 6 degrees
        minute_angle = 6 * minutes  # [web:5][web:7]
        
        # Absolute difference between the two angles
        diff = abs(hour_angle - minute_angle)  # [web:5]
        
        # Return the smaller angle (<= 180 degrees)
        return min(diff, 360 - diff)  # [web:5][web:8]
