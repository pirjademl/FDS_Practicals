# IN second year engineering computer engineerinng class of M students set of A students play cricket and set of B student play badminton .
#  Write a python program to find and display 
# 1 Set of students who play either cricket or badminton or both 
# 2 set if stuednt who play both cricket and badminton a intersection b
# 3 set of students who only play cricket 
# 4 set of students who only play badminton 
# 3 set of students who neither play cricket nor badminton 

def accept_set(A,str):
    n=int(input("Enter the total no of student who play %s:"%str)) 
    for i in range(n):
        nameOfStudent=input("Enter name of the student %d who play %s:"%(i+1),str)
        A.append(nameOfStudent)
    print("set accepted successfully ")

def displaySet(A,str):
    n=len(A);
    if n==0:
        print("\n group of student who play %s{ }"%str)
    else:
        print("Group of students who play %s"%str, end='')
        for i in range(n-1):
            print("%s,"%A[i] ,end='')
        print("%s,"%A[n-1] ,end='')


def searchSet(arr,keyToFind):
    for i in range(len(arr)):
        if (arr[i]==keyToFind):
            return 1
        else:
            return 0

def findIntersection(setA,setB,setC):
    for i in range(len(setA)):
        flag=searchSet(setB,setA[i])
        if(flag==1):
            setC.append(setA[i])


# function for finding the difference 
def findDifference(setA,setB,setC):
    for i in range(len(setA)):
        flag=searchSet(setB,setA[i])
        if(flag==0):
            setC.append(setA[i])

# function for findin the union 
def findUnion(setA,setB,setC):
    for i in range(len(setA)):
        setC.append(setA[i])
    for i in range(len(setB)):
        flag=searchSet(setA,setB[i])
        if(flag==0):
            setC.append(setB[i])

def main():
    groupA=[]
    groupB=[]
    groupC=[]
    while True:
        print("\n 1 Accept the information")
        print("\n 2 List of student who play both cricket and badminton")
        print("\n 3 List of student who play either cricket or badminton")
        print("\n 4 List of student who play neither cricket or badminton")
        print("\n 5 List of student who play  cricket or football but not badminton")
        print("\n 6 Exit")
        ch=int(input("Enter your choice"))
        groupR=[]
        if ch==6:
            print("End of the program")
        elif ch==1:
            accept_set(groupA,"cricket")
            accept_set(groupB,"badminton")
            accept_set(groupC,"football")
            displaySet(groupA,"cricket")
            displaySet(groupB,"badminton")
            displaySet(groupC,"football")
        elif ch==2:
            displaySet(groupA,"cricket")
            displaySet(groupB,"badminton")
            findIntersection(groupA,groupB,groupC)
            displaySet(groupR,"both cricket and badminton")
        elif ch==3:
            displaySet(groupA,"cricket")
            displaySet(groupB,"badminton")
            R1=[]
            findUnion(groupA,groupB,R1)
            R2=[]
            findIntersection(groupA,groupB,R2)
            findDifference(R1,R2,groupR)
            displaySet(groupR,"either cricket or badminton but not both")
        elif ch==4:
            displaySet(groupA,"cricket")
            displaySet(groupB,"badminton")
            displaySet(groupC,"football")
            R1=[]
            findUnion(groupA,groupB,R1)
            findDifference(groupC,R1,groupR)
            displaySet(groupR,"neither cricket nor badminton")
            print("Number of student who play neither cricket nor badminton is %d"%len(groupR)) 


if __name__ == "__main__":
    main()