"""a =[5,6,3,1,9,7,0]

temp=0
for i in range(len(a)):
    for j in range (i):
        if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
    print(a)"""
def rem(list, col_num):
    col = col_num-1
    for n1 in list:
        if(len(n1) >= col_num):
            n1.remove(n1[col])
        else:
            return False
    return list
col = int(input("Enter column to remove : "))
list = [[1,2,3],[2,4,5],[1,1,1]]
print("Original List : ")
print(list)
list = rem(list,col)
if list == False:
    print("Column number is greater than one of the nested list size : ")
else:
    print("Modified list: ")
    print(list)