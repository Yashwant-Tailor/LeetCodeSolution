import java.util.* ; 
class Solution {
    public int maximalRectangle(char[][] matrix) {
        var bar_height = new int [matrix.length][matrix[0].length] ;
        for(var col = 0 ; col < matrix[0].length ; col++){
            for(var row = matrix.length-1 ; row >= 0 ;row--){
                if(row+1 < matrix.length){
                    bar_height[row][col] += bar_height[row+1][col] ; 
                }
                if(matrix[row][col] == '1'){
                    bar_height[row][col]++;
                }
                else{
                    bar_height[row][col] = 0 ;
                }
            }
        }
        // for(var row = 0 ;  row < matrix.length ; row++){
        //     for(var col = 0 ; col < matrix[0].length ; col++){
        //         System.out.print(bar_height[row][col]+" ");
        //     }
        //     System.out.println();
        // }
        Deque<Integer> bar_stack = new ArrayDeque<Integer>() ; 
        var L = new int[matrix[0].length] ; 
        var R = new int [matrix[0].length] ;
        int rec_area_max = 0 ;
        for(var row = 0 ; row  < matrix.length ; row++){
            bar_stack.clear();
            for(var col = 0 ;col < matrix[0].length ; col++){
                while(!bar_stack.isEmpty() && bar_height[row][bar_stack.peekLast()] >= bar_height[row][col]){
                    bar_stack.pollLast();
                }
                if(bar_stack.isEmpty()){
                    L[col] = -1 ;
                }
                else{
                    L[col] = bar_stack.peekLast() ;
                }
                bar_stack.offerLast(col);
            }
            bar_stack.clear() ;
            for(var col = matrix[0].length-1; col >= 0 ;col--){
                while(!bar_stack.isEmpty() && bar_height[row][bar_stack.peekLast()] >= bar_height[row][col]){
                    bar_stack.pollLast();
                }
                if(bar_stack.isEmpty()){
                    R[col] = matrix[0].length ;
                }
                else{
                    R[col] = bar_stack.peekLast() ;
                }
                bar_stack.offerLast(col);
            }
            for(var col = 0 ; col < matrix[0].length ; col++){
                // System.out.print(col+"(L: " + L[col] + " R: "+ R[col]+") ");
                rec_area_max = Math.max(rec_area_max , (R[col] - L[col] - 1) * bar_height[row][col]);
            }
            // System.out.println(rec_area_max);
            
        }
        
        return rec_area_max ; 
        
    }
}
