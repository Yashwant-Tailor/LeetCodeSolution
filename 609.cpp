/*
do as it is .
simple implementation question
just use the container like hashmap to store the file name with same content
key =  content inside the file
value = file path
*/
class Solution {
public:
    map<string  , vector<string>>content_file ; 
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        int n = paths.size() ; 
        for(int i = 0 ; i < n ; i++){
            string directory = "" ;
            int j = 0 ; 
            int m = paths[i].size() ; 
            while(j < m && paths[i][j] != ' '){
                directory += paths[i][j] ; j++ ;
            }
            j++  ;
            while(j < m){
                string file_name = "" ; 
                while(j < m && paths[i][j]!= '('){
                    file_name+=paths[i][j] ; j++;
                }
                j++;
                string cont_file = "";
                while(j < m && paths[i][j]!=')'){
                    cont_file += paths[i][j] ; j++;
                }
                j++ ;
                j++;
                content_file[cont_file].push_back(directory+"/"+file_name) ; 
            }
        }
        vector<vector<string>>ans ; 
        for(map<string,vector<string>>::iterator it = content_file.begin() ; it != content_file.end()  ;it++){
            if(it->second.size() > 1)ans.push_back(it->second) ; 
        }
        return ans ; 
    }
};
