class Solution {
public:
    int maxArea(vector<int>& heights) {
        
        int l = 0;
        int r = heights.size()-1;
        int area = std::min(heights[l], heights[r]) * (r-l);


        while(l < r)
        {
            int current = std::min(heights[l], heights[r]) * (r-l);
            area = max(area, current);

            if(heights[l] < heights[r])
            {
                ++l;
            }
            else
            {
                --r;
            }

            
        }

        return area;
    }
};
