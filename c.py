for row  in range(7):
	for col in range(5):
		if( row in {0,6} and col in {1,2,3}):
			print('*',end=' ' )
		elif (row in {1,5} and col in {0,4} ) :	
			print('*',end= ' ')
		elif (row in {1,2,3,4} and col in {0}):	
			print('*',end=' ')
		else:
			print(' ',end= ' ')
	print()	