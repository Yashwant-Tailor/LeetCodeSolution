class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # Solution Overview
        # just simple iterate through the array and maintain the popularity and most viewed video id for each creator (we can take help of hashmap)
        from collections import defaultdict
        max_pop = 0
        creator_info = defaultdict(lambda : {'popularity':0,'max_view_vid':None,'max_view':None})
        for idx,creator in enumerate(creators):
            creator_info[creator]['popularity'] += views[idx]
            max_pop = max(max_pop,creator_info[creator]['popularity'])
            if creator_info[creator]['max_view'] is None or creator_info[creator]['max_view'] < views[idx]:
                creator_info[creator]['max_view'] = views[idx]
                creator_info[creator]['max_view_vid'] = ids[idx]
            elif creator_info[creator]['max_view'] == views[idx] and creator_info[creator]['max_view_vid'] > ids[idx]:
                creator_info[creator]['max_view_vid'] = ids[idx]
                
        ans = []
        for creator,info in creator_info.items():
            if max_pop == info['popularity']:
                ans.append([creator,info['max_view_vid']])
        return ans

