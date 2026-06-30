class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = nums.size();
        std::unordered_set<int> mums;
        for (int i = 0; i < l; i++){
            if (mums.find(target-nums[i]) != mums.end()){
                auto f = std::ranges::find(nums,target-nums[i]);
                int j = std::distance(nums.begin(),f);
                return {i,j};
            }
            else{
                mums.insert(nums[i]);
            }
        }
        return {};
    }
};