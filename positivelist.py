list1=[]
a= int(input("enter the number of elements:"))
for i in range(0,a):
    ele=int(input())
    list1.append(ele)
print(list1)
for  list2 in list1:
    if list2>=0:
        print(list2, end=" ")
