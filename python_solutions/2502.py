class Allocator:

    def __init__(self, n: int):
        # Solution Overview
        # we can simply maintain allocation information for every memory unit
        # in this case we will need O(n) space to store the information
        # one improvement on this solution would be to use bitmap to store the allocation information 
        # then we will need only n bits to store that information
        # other solution would be instead of maintaining the information for every memory unit 
        # we could maintain the information per memory block (consecutive allocated or free memory units)
        # in worst case this solution will also have the spce complexity of O(n)


        self.free_mem = {0:n}
        self.alloc_mem = {}

        

    def allocate(self, size: int, mID: int) -> int:
        first_idx = None
        for free_mem_idx,sz in self.free_mem.items():
            if sz >= size and (first_idx is None or first_idx > free_mem_idx):
                first_idx = free_mem_idx
        if first_idx is None:
            return -1
        sz = self.free_mem.pop(first_idx)
        sz -= size
        if sz > 0:
            self.free_mem[first_idx + size] = sz
        if mID not in self.alloc_mem:
            self.alloc_mem[mID] = []
        self.alloc_mem[mID].append([first_idx,size])
        return first_idx
            
        

    def free(self, mID: int) -> int:
        if mID not in self.alloc_mem:
            return 0
        loc = self.alloc_mem.pop(mID)
        total_freed_mem = 0
        for free_mem_idx , sz in loc:
            next_free_idx = free_mem_idx + sz
            total_freed_mem += sz
            if next_free_idx in self.free_mem:
                sz += self.free_mem.pop(next_free_idx)
            self.free_mem[free_mem_idx] = sz
        loc = list(self.free_mem.items())
        for free_mem_idx , sz in loc:
            next_free_idx = free_mem_idx + sz
            if next_free_idx in self.free_mem:
                sz += self.free_mem.pop(next_free_idx)
                # Point To remember 
                self.free_mem[free_mem_idx] = sz
        return total_freed_mem
        

        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
