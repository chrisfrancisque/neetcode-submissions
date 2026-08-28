class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        std::vector<int> result(temperatures.size(), 0);

        std::stack<pair<int, int>> temps;

        for(int i = 0; i < temperatures.size(); ++i ){
        int t = temperatures[i];
        while(!temps.empty() && t > temps.top().first){
            auto pair = temps.top();
            temps.pop();
            result[pair.second] = i - pair.second;
            
        } 
        
        temps.push({t, i});
        }

        return result;
    }
};
