def accept_array(arr):
    n=int(input("Enter total no of students"))
    for i in range(n):
        studentRoll=int(input("Enter the roll no of student %d "%(i+1)))
        arr.append(studentRoll)
    print("Student info accepted Successfully")
    return n
def display(arr,max):
    for i in range(max):
        print("%d"   %arr[i], end=' ')
    print('\n')
def linearSearch(arr,keyToFind):
    for i in range(len(arr)):
        if arr[i]==keyToFind:
            return  i
    return -1

def sentinelSearch(arr,max,keyToFind):
    last=arr[max-1]
    i=0
    arr[max-1]=keyToFind
    while(arr[i]!=keyToFind):
        i+=1
    arr[max-1]=last
    if(i<max-1 or (keyToFind==arr[max-1])):
        return i
    else:
        return -1
    
        
def main():
    a=[]
    while True:
        print("\n 1 Accept and display student information")
        print("\n 2 Linear Search")
        print("\n 3 Sentinel Search")
        print("\n 4 Exit")
        choice=int(input("Enter your choice"))
        if choice==4:
            quit()
        elif choice==1:
            n= accept_array(a)
            display(a,n)
        elif choice==2:
             rollToSearch=int(input("Enter the roll no to be searched"))
             result=linearSearch(a,rollToSearch)
             if result==-1:
                 print("ROll no to be searched is not found Hmm you are absent ")
             else:
                 print("Roll no to be searched is found at the ",result+1,"Location")
        elif choice==3:
             rollToSearch=int(input("Enter the roll no to be searched"))
             result=sentinelSearch(a,n,rollToSearch)
             if result==-1:
                 print("ROll no to be searched is not found Hmm you are absent ")
             else:
                 print("Roll no to be searched is found at the ",result+1,"Location")
        else:
            print("WRong choice entered ")


if __name__=="__main__":
    main()