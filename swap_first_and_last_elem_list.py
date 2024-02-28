myList = [10,20,30,40,50,60,70,80,90,100]
size=len(myList)

temp=myList[0]
myList[0]=myList[size-1]
myList[size-1]=temp

print("after swaping : ",myList)