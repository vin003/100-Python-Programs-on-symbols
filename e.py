for row in range(7):
	for col in range(5):
		if(row in {0,3,6}):
			print('*',end=' ')
		elif (row in {1,2,4,5} and col in {0n}):
			print('*', end=' ' )
		else:
			print(' ',end=' ')
	print()		