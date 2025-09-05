class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res_str= s[::-1]
        count = 0
        for i in range(len(res_str)):
            if count!=0 and i!=0 and res_str[i]==" ":
                return count
            elif res_str[i]!= " ":
                count+=1
        return count
        