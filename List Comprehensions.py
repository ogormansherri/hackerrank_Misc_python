# Enter your code here. Read input from STDIN. Print output to STDOUT
##List Comprehensions

#Getting ready for input
import fileinput

#Input
A, B, C, N = map(int, fileinput.input())

#Solve Cuboids: Generating combinations
my_arr = [[a, b, c] for a in range(A+1) for b in range(B+1) for c in range(C+1) if a + b + c != N]

#Output
print(my_arr)
