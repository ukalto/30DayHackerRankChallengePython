# Write your code here
class Day17:
    @staticmethod
    def power(n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")
        else:
            return n**p


myCalculator = Day17()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
