#Recursive algorithm to find exponentiation by sqauring:
#Ref : en.wikipedia.org/wiki/Exponentiation_by_squaring

def exp_by_squaring(x,n):
	if n<0:
		return exp_by_squaring((1/x),-n)
	elif n==0:
		return 1
	elif n==1:
		return x
	elif n%2==0:
		return exp_by_squaring(x**2,n/2)
	else:
		return x*(exp_by_squaring(x**2,((n-1)/2)))
