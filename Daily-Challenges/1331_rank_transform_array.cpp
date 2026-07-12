class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) noexcept{

        std::set<int> ss (arr.begin(), arr.end());
        std::unordered_map<int, int> ranks;
        std::vector<int> ans;

        int i = 1;
        for (int nums: ss){
            ranks.insert({nums,i++});
        }

        for (int nums: arr){
            ans.push_back(ranks[nums]);
        }

        return ans;
    }
};