
def binarySearch(array,low,high,x):
    if low<=high:
        mid = (low+high)//2
        if(array[mid] == x): 
            return mid 
        elif array[mid]>x: 
            return binarySearch(array,low,mid-1,x)
        else: 
            return binarySearch(array,mid+1,high,x)
    else: return -1

def main():
    n = int(input("Enter number of element in array: "))  
    array = []
    i = 0
    print("Enter elements: ")
    while i<n:
        a = int(input())
        array.append(a)
        i=i+1
    find = int(input("Element to search? "))
    x = binarySearch(array,0,n-1,find)
    if x == -1:
        print("Element not found in array")
        return
    print(f"Element found at position: {x+1}")

main()