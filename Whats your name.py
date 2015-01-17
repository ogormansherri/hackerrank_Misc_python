# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

#names
f_name, l_name = fileinput.input()
f_name = f_name.strip()
l_name = l_name.strip()

#output
print("Hello %s %s! You just delved into python." % (f_name, l_name))
