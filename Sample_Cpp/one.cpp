bin = 0
p = 0
q = 0
r = 0
x = 0
bin=1
q=0
print("\t\t\tDisplay pascal Triangle",end='')
print("\n\n\nHow Many Row Do you want to input:",end='')
r = int(input())
print("\nPascal's Triangle:\n",end='')
while(q<r):
	for p in range (40-3*q,0,-1):
		print(" ",end='')
	for x in range (0,q+1,1):
		if(x==0 or q==0):
			bin=1
		else :
			bin=(bin*(q-x+1))/x
		print("      ",end='')
		print(int(bin),end='')
	print("\n\n\n",end='')
	q += 1
input()
