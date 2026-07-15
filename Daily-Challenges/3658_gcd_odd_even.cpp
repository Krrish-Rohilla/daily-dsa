int gcd(int a, int b){
    while (b){
        int r = a % b;
        a = b;
        b = r;      // Euclidean Algorithm
    }
    return a;
}
class Solution {
public:
    int gcdOfOddEvenSums(int n) {
        int sumOdd = std::pow(n, 2);
        int sumEven = n * (n + 1);

        return gcd(sumOdd, sumEven);
    }
};