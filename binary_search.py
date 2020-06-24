def binary_search_recursive(l, x, left, right):
	if left>right:
		print("Not found")
	mid = left + (right-left)//2
	if l[mid]==x:
		print(str(x) + " found at " + str(mid))
	elif l[mid] > x:
		binary_search_recursive(l, x, left, mid-1)
	else: binary_search_recursive(l, x, mid+1, right)

def binary_search_iterative(l, x, right):
	left = 0
	while(left<=right):
		mid = left+(right-left)//2
		if l[mid]==x:
			return '{} found at index {}'.format(x,mid)
		elif l[mid]<x:
			left = mid+1
		else: right = mid-1
	return 'not found'




if __name__ == '__main__':
	l = [1,5,7,8,12,34,65,99]
	x, y = 34, 122
	#binary_search_recursive(l,x,0,len(l)-1)
	print(binary_search_iterative(l,y,len(l)-1))
	