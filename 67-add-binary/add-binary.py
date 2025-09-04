class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        print(f'length is {i} and {j}')
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            print(f'carry is {carry}')
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            print(total,result)
            carry = total // 2
        
        return ''.join(reversed(result))