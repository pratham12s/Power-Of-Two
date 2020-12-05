class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        multiple=2
        answer=-10
        if n<0:
            return False
        if n==1:
            return True
        while multiple<=n:
            answer=n/multiple
            multiple*=2
        return answer==1