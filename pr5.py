# write a python Program to store first percentage of student in array . 
#  WRite a function for sorting array of floating point in ascending order using 
# selection sort
# Bubble sort 


# Function to accept an array 
def acceptArray(arr):
    max=int(input("Enter total no of student "))
    for i in range(max):
        marksOfStudent=float(input("Enter the First year percentage of student"))
        arr.append(marksOfStudent)
    print("Details accepted succesfully")

# Function to display the array
def displayArray(arr):
    max=len(arr)
    if(max==0):
        print("No reords found in the database")
    else:
        print("Array of FE Marks   :",end=" ")
        for i in range(max):
            print("%.2f"%arr[i], end=" ")
        print("\n")


def selectionSort(arr):
    max=len(arr)
    for index in range(max-1):
        min_index=index
        for j in range(index+1,max):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[index],arr[min_index]=arr[min_index],arr[index]

 # Function for the bubble sort 
def bubbleSort(arr):
    max=len(arr)
    for index in range(1,max):
        for j in range(max-index):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


# main function

def main():
    Array=[]
    while True:
        print("\n 1 to accept and display the FE marks")
        print("\n 2 selection sort asending order")
        print("\n 3 bubble sort Descending order and display top five scores")
        print("\n 4 exit")
        choice=int(input("Enter your choice "))
        if choice==4:
            quit()
        elif choice ==1:
            acceptArray(Array)
            displayArray(Array)
        elif choice==2:
            print("Marks before sorting ")
            displayArray(Array)
            print("Marks after sorting")
            selectionSort(Array)
            displayArray(Array) 
        elif choice==3:
           print("Marks before sorting ")
           displayArray(Array)
           print("Marks after sorting")
           selectionSort(Array)
           displayArray(Array)     
           max=len(Array)
           if(max>=5):
               print("Top Five scores")
               for i in range(5):
                   print("%.2f"%Array[i])
           else:
               print("Top scores")
               for i in range(max):
                   print("%.2f"%Array[i]) 
        else:
            print("Wrong choice entered please try again")    
if __name__=="__main__":
    main()            