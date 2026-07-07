class Solution {
public:
    long long sumAndMultiply(int n) noexcept{
        int n_copy = n;
        int sum = 0;
        long long rev_ans = 0, ans = 0;
        while (n_copy){
            int digit = n_copy % 10;
            if (digit){
                sum += digit;
                rev_ans = (rev_ans * 10) + digit;
            }
            n_copy /= 10;
        }

        while(rev_ans){
            int digit = rev_ans % 10;
            ans = (ans * 10) + digit;
            rev_ans /= 10;
        }

        return (ans * sum);
    }
};