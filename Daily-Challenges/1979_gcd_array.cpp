int gcd(int a, int b) noexcept {
    while (b){
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}
class Solution {
public:
    int findGCD(vector<int>& nums) {
        auto a = std::min_element(nums.begin(), nums.end());
        auto b = std::max_element(nums.begin(), nums.end());

        return gcd(*a, *b);
    }
};