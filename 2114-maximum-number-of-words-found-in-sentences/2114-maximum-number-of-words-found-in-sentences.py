class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for words in sentences:
            count=1
            for ch in words:
                if ch==' ':
                    count+=1
            maxi=max(maxi,count)
        return maxi