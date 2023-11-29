def acceptArray(arr):
    max=int(input("Enter total no of students "))
    for i in range(max):
        percentage=float(input("Enter first year percentage of the student %d:1 "%(i+1)))
        arr.append(percentage)
    print("Details saved successfully")



# Display function
def display(arr):
    max=len(arr)
    if max==0:
        print("No records found in the database")
    print("First year percentage of studennts")
    for i in range(len(arr)):
        print("%.2f"%arr[i] )
    

def partition(arr,start, last):
    

    #choose the pivot 
    pivot=arr[last]
    i=start-1
    for j in range(start,last):
        if(arr[j]<pivot):
            i+=1

            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[last])=(arr[last],arr[i+1])
    return i+1



def quickSort(arr,start,last):
    if(start<last):
        pi=partition(arr,start,last)

        quickSort(arr,start,pi-1)

        quickSort(arr,pi+1,last)


def main():
    Array=[]
    while True:
        print("1 Accept and display the FE marks")
        print("2 Quick sort ascending order and display top five scores")
        print("3 exit")
        choice =int(input("Enter your choice"))
        if choice==3:
            quit()
        elif choice==1:
            acceptArray(Array)
            display(Array)
        elif choice==2:
            print("Marks before sorting ")
            display(Array)
            max=len(Array)
            quickSort(Array,0,max-1)
            print("Marks after sorting")
            display(Array)
            if (max-1>5):
                print(max-1,max-6)
                for i in range(max-1,max-6,-1):
                    print("\t %.2f"%Array[i])
            else:
                print("Top scores")
                for i in range(max-1,-1,-1):
                     print("\t %.2f"%Array[i])
        else:
            print("Wrong choice enter again !!!! try again")
if __name__=="__main__":
    main()