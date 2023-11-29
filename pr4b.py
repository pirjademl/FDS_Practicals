def accept_details(arr):
    max=int(input("Enter total no of students"))
    for i in range(max):
        studentRollNo=int(input("Enter roll no of student"))
        arr.append(studentRollNo)
    print("Details accepted successfully")
    return max

def display(arr,max):
    if max==0:
        print("There are no records in the database")
    for i in range(max):
        print("%d"%arr[i])
    print("\n")
def binarySearch(arr,start,end,keyToFind):
    if(start<=end):
        mid=int(start+end/2)
        if mid==keyToFind:
            return mid # Best case
        else:
            if(mid>keyToFind):
                return binarySearch(arr,start,mid-1,keyToFind)
            else:
                return binarySearch(arr,mid+1,end,keyToFind)
    return -1

def iterativeBinarySearch(arr,max,keyToFind):
    start=0
    end=max-1
    while (start<=end):
        mid=(start+end/2)
        if(mid==keyToFind):
            return mid #element found here in the best case
        else:
            if(mid>keyToFind):
                start=mid+1
            else:
                end=mid-1
    return -1 # not Found nahi mila 
def factorailSearch(arr,max,keyToFind):
    f1=0
    f2=1
    f3=f1+f2
    offset=-1
    while(f3<max):
        f1=f2
        f2=f3
        f3=f1+f2
        

