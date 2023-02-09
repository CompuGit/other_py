bm = int(input("Enter Born Month : "))
by = int(input("Enter Born Year : "))

cm = int(input("Enter Current Month : "))
cy = int(input("Enter Current Year : "))

ageYears = cy-by
ageMonths = cm-bm
if(ageMonths < 0):
	ageMonths+=12
	ageYears-=1
	
print('\nThe age of PERSON is :',ageYears,'Years and',ageMonths,' Months')

if(ageYears>=18 and ageMonths>=0):
	print('\nEligible for Vote')
else:
        print('\nNot Eligiblefor Vote')

