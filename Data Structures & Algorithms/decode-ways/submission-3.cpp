class Solution {
public:
    int numDecodings(string s) {
        int dp[100];

        dp[0]=1;
        
        if(s[0]=='0'){
            dp[0]=0;
            dp[1]=0;
        }
        else if(s[1]=='0'){
            
                dp[0]=1;
                dp[1]=0;
            if(s[0]=='1' or s[0]=='2'){
                dp[1]=1;
                }
        }
        else if(s[0]=='1' or (s[0]=='2' and s[1]<='6')){
            dp[1]=2;
        }else{
            dp[1]=1;
        }
        
        for(int i=2;i<s.size();i++){
            if(s[i]=='0' ){
                if(s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6')){
                dp[i]=dp[i-2];}
                else{
                    dp[i]=0;
                }
            }
            else if(s[i-1]=='1' or (s[i-1]=='2' and s[i]<='6')){
                dp[i]=dp[i-1]+dp[i-2];
            }
            else{
                dp[i]=dp[i-1];
            }
            
        }
        return dp[s.size()-1];
    }
};
