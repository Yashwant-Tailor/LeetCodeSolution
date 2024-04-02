class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int drunk = 0 ;
        while (numBottles > 0){
            if (numBottles >= numExchange){
                drunk += numExchange ; 
                numBottles -= numExchange ; 
                numBottles += 1 ;
                numExchange += 1 ;
            }
            else{
                drunk += numBottles ; 
                numBottles = 0;
            }
        }
        return drunk ;
    }
};
