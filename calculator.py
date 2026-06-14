a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=input('add/subtract/multiply/divide:')
if c=='add':
	print('sum',a+b)
elif c=='subtract':
	print('difference',a-b)
elif c=='multiply':
	print('product',a*b)
else:
	print('quotient',a/b)
print('completed')
