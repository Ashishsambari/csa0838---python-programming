#pgm to get no.of ways to climb the stairs..
def noOfWays(n):
    if n <= 1:
        return n
    else:
        return stair(n-1) + stair(n-2)
s=int(input("Enter N val :"))
print(noOfWays(s+1))
