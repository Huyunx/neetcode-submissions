//// shiiiiiiiiiit c++ is annoying
// I guess for new algorithms it is the most efficient to
// first make everything (any detail) clear on paper before implementing 

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<pair<int,int>> adj[101];  //[[node adjecent to n-th node ,time],[...]] 
       
        for (int i=0;i<times.size();i++){
            int u=times[i][0];
            int v=times[i][1];
            int t=times[i][2];
            adj[u].push_back({-t,v});
           


        }
        priority_queue<pair<int,int>> ordered_paths;
        ordered_paths.push({0,k});
        
        set<int> notvi;
        int mintoreach_node[101];
        for (int i=1;i<=n;i++){
            notvi.insert(i);
            mintoreach_node[i]=INT_MIN;
        }
        int ans=0;
     
        while (!ordered_paths.empty())
        {
            /* code */
            auto a = ordered_paths.top();
            ordered_paths.pop();
            int currt=a.first;
            int currnode=a.second;
            if(notvi.count(currnode)){//if currnode is not visited
                ans=min(ans,currt);//should use min instead of max to find the max absolute value
                notvi.erase(currnode);
            }
            for (auto [ti,node]:adj[currnode]){
                if(mintoreach_node[node]<currt+ti){
                    ordered_paths.push({currt+ti,node});
                    mintoreach_node[node]=currt+ti;
                }
            }

        }
        if(!notvi.empty()){
            return -1;
        }
        return -ans;
        


    }
};//disaster hah,i am stupiddddddddd(no)
