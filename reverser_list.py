myList=[10,15,20,24,36,12,98,6,4,5,6,9,8]
print(myList)
reverse_list=[]
for i in range(len(myList)-1,-1,-1):
    reverse_list.append(myList[i])
   
print("Reversed list is:",reverse_list)


