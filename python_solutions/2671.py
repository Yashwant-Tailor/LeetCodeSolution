class FrequencyTracker:
    # Solution Overview
    # use two dicitonary to keep track of frequency of each element 
    # and count of each unique frequency
    def __init__(self):
        from collections import defaultdict
        self.num_freq = defaultdict(lambda : 0)
        self.freq_freq = defaultdict(lambda : 0)
        

    def add(self, number: int) -> None:
        prev_freq = self.num_freq[number]
        if prev_freq > 0:
            self.freq_freq[prev_freq] -= 1
        curr_freq = prev_freq + 1
        self.num_freq[number] = curr_freq
        self.freq_freq[curr_freq] += 1

    def deleteOne(self, number: int) -> None:
        prev_freq = self.num_freq[number]
        if prev_freq > 0:
            self.freq_freq[prev_freq] -= 1
            curr_freq = prev_freq - 1
            self.num_freq[number] = curr_freq
            if curr_freq > 0:
                self.freq_freq[curr_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        if self.freq_freq[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
