class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            dupList = []
            if len(res)<=1:
                for k in range(len(res)+1):
                    dupList.append(1)
                res.append(dupList)
            else:
                recLst = res[len(res)-1]
                for j in range(len(recLst)+1):
                    if j==0 or j==(len(recLst)):
                        dupList.append(1)
                    else:
                        dupList.append(recLst[j-1]+recLst[j])
                res.append(dupList)
        return res[rowIndex]
        