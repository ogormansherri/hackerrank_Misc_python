# Enter your code here. Read input from STDIN. Print output to STDOUT
##Exchanging integers

#preparing for input
import fileinput

#Input
x, y = fileinput.input()

#Swap and solve 
x, y = (y, x)

#Display the output
print(x)
print(y)
