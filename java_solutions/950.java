import java.util.* ; 
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Queue<Integer> ind = new ArrayDeque<Integer>();
        Arrays.sort(deck) ; 
        for(int i = 0 ; i < deck.length ; i++){
            ind.offer(i);
        }
        int [] new_deck = new int[deck.length];
        for(var num : deck){
            var idx = ind.poll();
            new_deck[idx] = num ; 
            if (ind.size() > 0){
                idx = ind.poll();
                ind.offer(idx);
            }
        }
        return new_deck ; 
    }
}
