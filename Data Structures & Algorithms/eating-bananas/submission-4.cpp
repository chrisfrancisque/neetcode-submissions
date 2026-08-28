class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int high = *max_element(piles.begin(), piles.end());
        int low = 1;
        int minSpeed = high;

        while(low <= high){
            int mid = (low+high)/2;


            int runningTotal = 0;
            for(int p : piles){
                int num = ceil(static_cast<double>(p) / mid);
                runningTotal += num;
            }

            if(runningTotal <= h){
                minSpeed = min(minSpeed, mid);

                high = mid-1;
            }
            else if(runningTotal > h){
                low = mid + 1;
            }


        }

        return minSpeed;
        
    }
};
