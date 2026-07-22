class Solution {
    
private:
    bool dfs(int i,int j,vector<vector<char>>& board,map<pair<int,int>,bool>& visited,
    vector<pair<int,int>>& cells){
        //return whether i,j is in full surrounded region 
        if(i>=board.size() or j>=board[0].size() or i<0 or j<0){
            return 0;
        }
        if(board[i][j]=='X' or visited[{i,j}]){
            return 1;
        }

        visited[{i,j}]=1;
        bool a= dfs(i+1,j,board,visited,cells);
        bool b= dfs(i-1,j,board,visited,cells);
        bool c= dfs(i,j+1,board,visited,cells);
        bool d= dfs(i,j-1,board,visited,cells);
        bool yes=a and b and c and d;
        cells.push_back({i,j});

        return yes;
    }
public:
    void solve(vector<vector<char>>& board) {
        map<pair<int,int>,bool> visited;
        for (int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                visited[{i,j}]=0;
                
            }
        }
        for (int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(board[i][j]=='O' and !visited[{i,j}] ){
                    vector<pair<int,int> > cells;
                    if(dfs(i,j,board,visited,cells)){
                    for (auto [x,y]:cells){
                        board[x][y]='X';
                    }}
                
                }
            }
        }

    }
};
