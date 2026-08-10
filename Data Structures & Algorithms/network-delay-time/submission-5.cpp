class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<pair<int,int>> adj[101];
        priority_queue<pair<int, int>,
               vector<pair<int, int>>,
               greater<pair<int, int>>> heap;
        for (int i=0;i<times.size();i++){
            int u=times[i][0];
            int v=times[i][1];
            int w=times[i][2];
            adj[u].push_back({w,v});
        }
        heap.push({0,k});
        set<int> visited;
       
        int ans=0;
        while (!heap.empty()){
            pair<int,int> a = heap.top();
            heap.pop();
                      
            int shortestpath=a.first;
            int node=a.second;
            if(visited.count(node)){
                continue;
            }
            ans=shortestpath;
            visited.insert(node); 
            for (int i=0;i<adj[node].size();i++){
                int wei=adj[node][i].first;
                int nextnode=adj[node][i].second;
                heap.push({shortestpath+wei,nextnode});
            }
        }
        if(visited.size()!=n){
            return -1;
        }
        return ans;

    }
};
