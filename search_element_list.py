list = ["a", "b", "c", "d", "e"]
element = str(input("give the string :- "))

index = -1
for i in range(len(list)):
    if list[i] == element:
        index = i
        break

if index != -1:
    print("The element is at index", index)
else:
    print("The element is not in the list.")