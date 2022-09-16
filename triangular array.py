def solve(n):
    for i in range(n+1):
        for j in range(n-i):
            print(' ',end='')
        C=1
        for j in range(1,i+1):
            print(C,' ',sep='',end='')
            C=C*(i-j)//j
        print()

class PascalTriangle :

	def sumPascalRow(self, n) :
		if (n <= 0) :
			return
		
		print("\n Row ", n+1," ")

		sum = (1 << n)
		print(" Sum : ", sum ," ")
	
b=int(input())
a=int(input())
solve(b)
def main() :
    task = PascalTriangle()
    task.sumPascalRow(a-1)

if __name__ == "__main__": main()
