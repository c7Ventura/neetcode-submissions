class Solution {
public:
    //two pointer approach
    bool isAnagram(string s, string t) {
        //early check
        if (s.length() != t.length())
            return false;
        unordered_map<char, int> sMap;
        for(int i = 0; i < s.length(); i++) {
            sMap[s[i]]++;
        }
        unordered_map<char, int> tMap;
        for(int j = 0; j < t.length(); j++) {
            tMap[t[j]]++;
        }

        // go through dictionary 
        for(const auto& [key, value] : sMap) {
            //ensure K/V pairs have same count. If not, return false
            if(tMap[key] != value)
                return false;
        }
        // nothing detected. return true.
        return true;
    }
};
