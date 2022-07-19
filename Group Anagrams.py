# TC: if m is the length of the words, and n is the length of the list, then the time complexity will be of the order O(m^2 * n * log m)

# SC: We are creating a unique list of strings present in the list. The worst case scenario will be : all the strings in the list are unique. therefore the space complexity is O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        
        for i in strs:
            sorted_i = "".join(sorted(i))
            
            if sorted_i not in hashmap:
                hashmap[sorted_i] = [i]
            else:
                hashmap[sorted_i].append(i)
            
        return hashmap.values()
            