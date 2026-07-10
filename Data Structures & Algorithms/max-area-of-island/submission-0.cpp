class Solution {
private:
    int area(int i,int j,vector<vector<int>>& grid){
        if(i<0 or j<0 or i>=grid.size() or j>=grid[0].size() or grid[i][j]==0){
            return 0;
        }
        grid[i][j]=0;
        return 1+area(i+1,j,grid)+area(i,j+1,grid)+area(i-1,j,grid)+area(i,j-1,grid);
        
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans=0;
        for(int i=0;i<grid.size();i++){
            for (int j=0;j<grid[0].size();j++){
                if(grid[i][j]==1){
                    ans=max(ans,area(i,j,grid));
                }
            }
        } 
        return ans;
    }
};
