array = [1, 2, 3, 4, 5]
element = int(input("enter the number :- "))

index = -1
for i in range(len(array)):
    if array[i] == element:
        index = i
        break

if index != -1:
    print("The element is at index", index)
else:
    print("The element is not in the array.")