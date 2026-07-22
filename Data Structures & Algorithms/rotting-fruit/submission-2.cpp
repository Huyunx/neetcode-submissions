class Solution {
//depth of multi bfs
private:
    bool ok(int a,int b,vector<vector<int>>& grid){
        if(a>=grid.size() or a<0 or b<0 or b>=grid[0].size() or grid[a][b]!=1){
            return 0;
        }else{
            return 1;
        }

    }
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ans=0;
        queue<pair<int,int>> q;
        bool visited[grid.size()][grid[0].size()];
        for (int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                if(grid[i][j]==2){
                    q.push({i,j});
             
                    visited[i][j]=0;
                }
            }
        }
        //bfs
        
        while (!q.empty()){
          
            //go through the rottens at this level add the next level
            int repe=q.size();
            for (int i=0;i<repe;i++){//,repeating times: whatever is the size of queue 
                int a=q.front().first;
                int b=q.front().second;
                if(ok(a+1,b,grid)){
                    q.push({a+1,b});
                    grid[a+1][b]=2;
                }
                if(ok(a-1,b,grid)){
                    q.push({a-1,b});
                    grid[a-1][b]=2;
                }
                if(ok(a,b+1,grid)){
                    q.push({a,b+1});
                    grid[a][b+1]=2;
                }
                if(ok(a,b-1,grid)){
                    q.push({a,b-1});
                    grid[a][b-1]=2;
                }

                q.pop();
               
            }
            ans++;
        }
        for (int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                if(grid[i][j]==1){
                    return -1;
                }
            }
        }
        if (ans==0) {return 0;}
        else{
            return ans-1;
        }
    }
};
