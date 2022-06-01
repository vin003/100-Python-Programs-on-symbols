for row in range(7):
	for col in range(5):
		print('* ',end=' ')
	print()

for row in range(7):
	for col in range(5):
		if (col ==0 or col==4):
			print('* ',end=' ')
		else:
			print(' ',end =' ')
	print()	
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ')	
for i in range(7):
		for col in range(5):
			if (i==0 or i==6):
				print('*',end=' ')
			elif (i in {1,2,3,4,5} and col in {0,4} ):
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()		
				

for i in range(7):
		for col in range(5):
			if (i==0 or i==6):
				print('*',end=' ')
			elif (col == 0 or col == 4):
				print('*',end=' ')
			else:
				print(' ',end=' ')
		print()		
					
	
	