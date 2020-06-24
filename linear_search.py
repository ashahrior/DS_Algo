import math

def linear_search(l,n):
	for i in range(len(l)):
		if l[i]==n:
			return str(n)+" found at "+str(i+1)
	return "not found"



if __name__ == '__main__':
	l = [1,5,0,8,5]
	n = 5
	print(linear_search(l,n))
	print()
	