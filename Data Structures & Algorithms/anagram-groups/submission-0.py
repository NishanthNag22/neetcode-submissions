class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for i in range(len(strs)):
            sorted_word="".join(sorted(strs[i]))
            if sorted_word not in anagrams:
                anagrams[sorted_word]=[]
            anagrams[sorted_word].append(strs[i])
        return list(anagrams.values())