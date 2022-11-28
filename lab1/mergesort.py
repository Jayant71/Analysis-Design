def mergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        low = array[:mid]
        high = array[mid:]

        mergeSort(low)
        mergeSort(high)
        i=j=k=0       
        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                array[k]=low[i]
                i=i+1
            else:
                array[k]=high[j]
                j=j+1
            k=k+1

        while i < len(low):
            array[k]=low[i]
            i=i+1
            k=k+1

        while j < len(high):
            array[k]=high[j]
            j=j+1
            k=k+1

def main():
    n = int(input("Enter number of element in array: "))  
    array = []
    i = 0
    print("Enter elements: ")
    while i<n:
        a = int(input())
        array.append(a)
        i=i+1
    print(array)
    mergeSort(array)
    print(array)

main()
