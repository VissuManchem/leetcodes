class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = [[] for i in range(len(nums)+1)]
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        for c, v in count.items():
            new[v].append(c)

        print(new)
        final = []
        for i in range(len(new)-1, -1, -1):
            
            #print(len(new[i]))
            
            for j in new[i]:
                #print(final)
                final.append(j)
                #print(final)
                if len(final) == k:
                    return final