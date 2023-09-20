tot=0
mark=[]
subject=int(input('Enter no of subject:'))
for num in range(subject):
   marks=int(input("subject marks is:"))
   mark.append(marks)
   tot=tot+marks
   if marks>35:
        print("Pass")
   else:
        print('Fail')     
print('Total mark is:',tot)         