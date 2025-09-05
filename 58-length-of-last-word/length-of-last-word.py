class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res_str= s[::-1].strip()
        count = 0
        for i in range(len(res_str)):
            if res_str[i]== " ":
                break
            count+=1
        return count
        