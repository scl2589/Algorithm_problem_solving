class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for str in strs:
            word = ''.join(sorted(str))
            dictionary[word].append(str)
        return dictionary.values()