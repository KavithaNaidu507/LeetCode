class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans=[]
        n=len(p)
        m=len(s)
        freq={}
        char={}
        for ch in p:
            freq[ch]=freq.get(ch,0)+1 
        for i in range(len(s)):
            char[s[i]]=char.get(s[i],0)+1 
            if i>=n:
                char[s[i-n]]-=1
                if char[s[i-n]]==0:
                    del char[s[i-n]]
            if char==freq:
                ans.append(i-n+1)
        return ans