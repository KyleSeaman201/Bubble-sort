#This function is a bubble sort algorithm that inputs an unsorted list of numbers and returns a sorted list.
#This function also prints the state of the list after each pass.

def bubble_sort(numList):
        length= len(numList)
        count=0
        Sorted= False
        while not Sorted:
                for j in range(length-1):
                        temp= j+1
                        if numList[j] > numList[temp]:
                                numList[j], numList[temp] = numList[temp], numList[j]
                                count+=1
                print(numList)
                if count==0:
                        Sorted= True
                count=0
        return numList

#test cases
#bubble_sort([2, 3, 5, 4, 1])
