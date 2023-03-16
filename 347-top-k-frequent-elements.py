class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        #dict to store the frequency

        #iterate over the nums
            #map the frequency

        #sort the values of the dict by the greatest 
        
        #return the first k

        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        sorted_freq = sorted(freq.items(), reverse=True, key=lambda x: x[1])

        ans = []
        for item in sorted_freq[:k]:
            ans.append(item[0])
        return ans

        # T: O(n log n) because of the sorted
        # M: O(n) 
