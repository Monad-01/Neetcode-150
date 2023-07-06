class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # So the idea to this question is that we are able to create a hashMap
        # For the HashMap, the letters for each word is the key and will be represented in the list count [].
        # The trick here is knowing that you are able to track the letters by creating 26 indexes to represent
        # the letters. Then if you subtract ord("a") from the character selected, it will represent the index of that
        # character in the list.

        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            # We have to cast 'count' as a tuple because dict does not accept lists as a key :/
            ans[tuple(count)].append(s)

        return ans.values()
        
        