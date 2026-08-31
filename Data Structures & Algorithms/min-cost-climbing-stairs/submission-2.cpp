class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if(cost.size()==1){
            return cost[0];
            
        }
        if(cost.size()==2){
            return min(cost[0],cost[1]);
        }
 
        int l=cost.size();
        int preprev=0;
        int prev=0;
        for (int i=2;i<=l;i++){
            int a=prev;
            prev=min(prev+cost[i-1],preprev+cost[i-2]);
            preprev=a;
        }
        return prev;
    }
};
