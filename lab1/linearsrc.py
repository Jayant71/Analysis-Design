
def linearSearch(array,find):
    count = 1
    for i in array:
        if i==find:
            return count
        count = count + 1
    return 0

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
    x = linearSearch(array,find)
    if x == 0:
        print("Element not found in array")
        return
    print(f"Element found at position: {x}")

main()
