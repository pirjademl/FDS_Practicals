# Problem statement -Write a python program to store marks score for first test subject of c data structure and algorithms for n students compute
# 1 The average score of the class
# 2 Highest and lowest score of the class
# 3 marks scored by most of all student 
# 4 list of student who were absent for the test 
def accept_marks(arr):
    n=int(input("Enter the total no of students"))
    for i in range(n):
        while True:
            studentMarks=input("Enter marks scored in FDS for student %d "%(i+1))
            if studentMarks=="AB":
                studentMarks=-1
                break
            studentMarks=int(studentMarks)
            if(studentMarks>=0 and studentMarks<=30):
                break
            else:
                print("Enter valid marks out of 30")
        arr.append(studentMarks)
    print("Marks accepted successfully")
def displayMarks(marksArr):
    print("Marks scored inn FDS")
    for i in range(len(marksArr)):
        if(marksArr[i]==-1):
            print("student %d AB"%(i+1))
        else:
            print("student %d :%d"%(i+1,marksArr[i]))
def searchSet(arr,keyToFind):
    n=len(arr)
    for i in range(n):
        if arr[i]==keyToFind:
            return (1)
        else:
            return 0

def findAvg(arr):
    sum=0
    for i in range(len(arr)):
        if arr[i]!=-1:
            sum=sum+arr[i]
    avg=sum/len(arr)
    displayMarks(arr)
    print("\n Average score of class is %.2f\n\n"%avg)

def findHighestandLowest(arr):
    max=-1
    min=31
    max_ind=0
    min_ind=0
    for i in range(len(arr)):
        if(max<arr[i]):
            max=arr[i]
            max_ind=i
        if(min>arr[i] and arr[i]!=-1):
            min=arr[i]
            min_ind=i
    displayMarks(arr)
    print("Highest mark score of class is %d scored by student %d"%(max ,max_ind+1))
    print("lowest mark score of class is %d scored by student %d"%(min ,min_ind+1))
def absentCount(arr):
    count =0
    for i in range(len(arr)):
        if arr[i]==-1:
            count+=1
        displayMarks(arr)
    print("Absent students count ",count)
def displayWithHighFrequency(arr):
    freq=0
    Marks=0
    for i in range(len(arr)):
        count =0
        if arr[i]!=-1:
           for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
            if freq<count:
                Marks=arr[i]
                freq=count
    displayMarks(arr)
    print("Marks with highest frequency is %d (%d)"%(Marks ,freq))
def main():
    FDS_MARKS=[]
    while True:
        print("\n 1 Accept FDS Marks")
        print("\n 2 Average score for class")
        print("\n 3 highest and lowest score of class")
        print("\n 4 count of student who were absent for test")
        print("\n 5 Display mark with highest frequency ")
        print("\n 6 exit")
        ch=int(input("Enter your choice"))
        if ch==6:
            quit()
        elif ch==1:
            accept_marks(FDS_MARKS)
            displayMarks(FDS_MARKS)
        elif ch==2:
            findAvg(FDS_MARKS)
        elif ch==3:
            findHighestandLowest(FDS_MARKS)
        elif ch==4:
            absentCount(FDS_MARKS)
        elif ch==5:
            displayWithHighFrequency(FDS_MARKS)
        else:
            print("Wrong Choice entered ")

if __name__ == "__main__":
    main()
    

        