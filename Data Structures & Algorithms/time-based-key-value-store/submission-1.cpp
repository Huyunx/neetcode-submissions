class TimeMap {
public:
    unordered_map<string,vector<pair<int,string>>> mapp;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        mapp[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
        int l=0,r=mapp[key].size()-1;
        string ans="";
        while(1){
            int m=(l+r)/2;
            if(l>r){
                break;
            }
            if(mapp[key][m].first<=timestamp){
                ans=mapp[key][m].second;
                l=m+1;
            }
            if(mapp[key][m].first>timestamp){
                r=m-1;
            }
            
        }
        return ans;

    }
};
