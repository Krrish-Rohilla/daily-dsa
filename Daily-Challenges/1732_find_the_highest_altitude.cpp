class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> alt;
        alt.push_back(0);
        int s = 0;
        for(auto i = gain.begin(); i != gain.end(); i++){
            s += *i;
            alt.push_back(s);
        }
        return *max_element(alt.begin(),alt.end());
    }
};