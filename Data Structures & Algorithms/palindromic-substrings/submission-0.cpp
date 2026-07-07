class Solution {
public:
    int countSubstrings(string s) {
        int c=0;
        for(int i=0;i<=s.size();i++){
            int l=i,r=i;
            while (l>=0 and r<s.size() and s[l]==s[r]){
                c++;
                l--;
                r++;
                
            }

            l=i;
            r=i+1;
            while (l>=0 and r<s.size() and s[l]==s[r]){
                c++;
                l--;
                r++;
                
            }
        }
        return c;


    }
};
