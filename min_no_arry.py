arr=[10,20,64,99,10,88,63,74,36,95,78,65,32,14,52]
min=arr[0]

for i in range(0 ,len(arr)):
    if(arr[i]<min):
        min=arr[i]
    
    print("larget no in the given arry is " +str(min));