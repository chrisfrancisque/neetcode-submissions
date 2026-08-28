class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int min = prices[0];

        int max = 0;

        for(int i = 1; i < prices.size(); ++i)
        {
            min = std::min(prices[i], min);

            if(min < prices[i])
            {
                int current = prices[i] - min;
                max = std::max(max, current);
            }
        }
    
    return max;
        }
};
