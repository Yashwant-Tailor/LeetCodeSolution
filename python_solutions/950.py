from queue import SimpleQueue
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ind = SimpleQueue()
        for idx in range(len(deck)):
            ind.put(idx)
        deck.sort()
        new_deck = [-1 for i in range(len(deck))]
        for num in deck:
            idx = ind.get()
            new_deck[idx] = num
            if not ind.empty() :
                idx = ind.get()
                ind.put(idx)
        return new_deck
