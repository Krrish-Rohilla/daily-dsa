class Solution {
    public double angleClock(int hour, int minutes) {
        
        double hand1 = hour;
        if (hour == 12) hand1 = 0;
        hand1 += minutes/60.0;

        double hand2 = minutes/5.0;
        double angle = Math.abs(hand1 - hand2) * 30;

        if (angle <= 180) return angle;
        return 360 - angle;
    }
}