class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^a-zA-Z]', ' ',paragraph).lower().split()
        words = [word for word in words if word not in banned]
        count = collections.Counter(words)
        return count.most_common(1)[0][0]