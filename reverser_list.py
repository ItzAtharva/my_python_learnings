myList=['a','b','c',]
print(myList)
reverse_list=[]
for i in range(len(myList)-1,-1,-1):
    reverse_list.append(myList[i])
   
print("Reversed list is:",reverse_list)


