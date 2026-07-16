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
    long long gcdSum(vector<int>& nums) noexcept {
        long maxN = 0;
        std::vector<int> prefixGcd;
        prefixGcd.reserve(nums.size());

        for (int n: nums){
            maxN = std::max({maxN, (long)n});
            prefixGcd.push_back(gcd(n, maxN));
        }
        prefixGcd.shrink_to_fit();

        int l = nums.size();
        long long sum = 0;
        std::sort(prefixGcd.begin(), prefixGcd.end());

        for (int i = 0; i < l/2; i++){
            sum += gcd(prefixGcd[i], prefixGcd[l-i-1]);
        }
        return sum;
    }
};