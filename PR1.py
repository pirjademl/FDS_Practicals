# IN second year  computer engineerinng class of M students set of A students play cricket and set of B student play badminton .
#  write a python program to find and display 
# 1 Set of students who play either cricket or badminton or both 
# 2 set of stuednt who play both cricket and badminton a intersection b
# 3 set of students who only play cricket 
# 4 set of students who only play badminton 
# 3 set of students who neither play cricket nor badminton 
def accept(arr,str):
    n=int(input("Enter no of student who play %s"%str))
    for i in range(n):
        studentDetails=input("Enter name of the student who play %s:"%str)
        arr.append(studentDetails)
    print("Details accepted Successfully")

def display(arr,str):
    if(len(arr)==0):
        print("\n group of student who play  %s{}"%str)
    else:
        print("\n group of student who play %s"%str)
        for i in range(len(arr)):
            print(arr[i])
def searchSet(arr,key):
    if len(arr)==0:
        return
    else:
        for i in range(len(arr)):
            if(arr[i]==key):
                return 1
            else:   
                return 0
def findIntersection(arr1,arr2,arr3):
        for i in range(len(arr1)):
            flag=searchSet(arr2,arr1[i])
            if flag==1:
                arr3.append(arr1[i])

def findUnion(arr1,arr2,arr3):
    for i in range(len(arr1)):
        arr3.append(arr1[i])
    for i in range(len(arr2)):
        flag=searchSet(arr1,arr2[i])
        if flag==0:
            arr3.append(arr2[i])
def findIntersection(arr1,arr2,arr3):
    for i in range(len(arr1)):
        flag=searchSet(arr2,arr1[i])
        if flag==1:
            arr3.append(arr1[i])
def findDiffernence(arr1,arr2,arr3):
    for i in range(len(arr1)):
        flag=searchSet(arr2,arr1[i])
        if flag==0:
            arr3.append(arr1[i])
            
def main():
    groupA=[]
    groupB=[]
    groupC=[]
    print("\n Enter 1 to store the information")
    print("\n enter 2 to find out list of student who plays cricket and badminton both  ")
    print("\n 3 list of  students who plays either  cricket or  badminton   ")
    print("\n 4 list of  students who plays neither cricket nor badminton   ")
    print("\n 5 List of student who play  cricket or football but not badminton")
    print("\n 6 exit")
    groupR=[]
    while(True):
        ch=int(input("Enter your choice"))
        if ch==6:
            print("Program Finished")
        elif ch==1:
                accept(groupA,"cricket")
                accept(groupB,"badminton")
                accept(groupC,"football")
                display(groupA,"cricket")
                display(groupB,"badminton")
                display(groupC,"football")
                
        elif ch==2:
            display(groupA,"cricket")
            display(groupB,"badminton")
            findIntersection(groupA,groupB,groupR)
            display(groupR,"both Criket and badminto")
        elif ch==3:
            display(groupA,"Cricket")
            display(groupB,"badminton")
            unionArray=[]
            findUnion(groupA,groupB,unionArray)
            intesectionArray=[]
            findIntersection(groupA,groupB,intesectionArray)
            diff=[]
            findDiffernence(unionArray,intesectionArray,diff)
            display(diff,"student play either cricket or badminton but but not both ")
        elif ch==4:
            display(groupA,"Cricket")
            display(groupB,"Badminton")
            display(groupC,"football")
            unionArray=[]
            findUnion(groupA,groupB,unionArray)
            diffarray=[]
            findDiffernence(groupC,unionArray,diffarray)
            display(diffarray,"students who play neither cricket nor badminton")
        elif ch==5:
            display(groupA,"Cricket")
            display(groupC,"football")
            unionArray=[]
            findUnion(groupA,groupC,unionArray)
            diffarr=[]
            findDiffernence(unionArray,groupB,diffarr)
            print("student who play either cricket or football but not badminton ",diffarr)



if __name__=="__main__":
    main()