class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false; // negative numbers are always false

        int temp = x; // making copy of x so that we don't loose original value
        long ans = 0;
        while (temp){
            int digit = temp % 10;
            temp = temp / 10;
            ans = (ans * 10) + digit;
        }
        return ans == x;
    }
};