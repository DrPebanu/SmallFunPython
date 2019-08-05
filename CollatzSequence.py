def Collatz(n):
	if n%2 == 0:
		x = n//2
		print(x)
		return x
	else:
		x = 3*n+1
		print(x)
		return x

print("Enter a number")
try:
        number = int(input())
        n = number
        steps = 0
        while n != 1:
                n = Collatz(n)
                steps +=1

        print(f"It took {steps} steps for {number} to reach 1")
except ValueError:
        print("Must input a number")
