class Solution {
    public int trap(int[] height) {
        int [] LH_MAX = new int[height.length]  ;
        int seen_max_height = -1 ; 
        for(int i = 0 ; i < height.length ; i++){
            seen_max_height = Math.max(seen_max_height , height[i]) ; 
            LH_MAX[i] = seen_max_height ; 
        }
        int water_trapped = 0 ; 
        seen_max_height = -1 ; 
        for(int i = height.length-1 ; i >= 0 ; i--){
            seen_max_height = Math.max(seen_max_height , height[i]) ; 
            // System.out.println("H: "+ height[i] + " L: "+ LH_MAX[i] + " R: " + seen_max_height);
            water_trapped += Math.abs(height[i] - Math.min(seen_max_height , LH_MAX[i]));
        }
        return water_trapped ; 
    }
}
