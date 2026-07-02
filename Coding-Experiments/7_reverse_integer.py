class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        x=x[::-1]
        if "-" in x:
            x=x.replace("-","")
            x=- int(x)
        else :
            x=int(x)
        if x not in range(-2**31,2**31):
            return 0
        return x