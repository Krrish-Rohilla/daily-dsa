class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hand1 = hour if hour!=12 else 0
        hand1 += minutes/60
        hand2 = minutes/5
        diff = abs(hand1 - hand2)
        angle = diff*30
        return angle if angle <= 180 else 360 - angle