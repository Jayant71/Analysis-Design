
def bubble_sort(n,array):
    if n==0: return
    i = 1
    while i<n:
        if array[i]<array[i-1]:
            tmp = array[i]
            array[i] = array[i-1]
            array[i-1] =tmp
        i=i+1
    bubble_sort(n-1,array)


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
    bubble_sort(n, array)
    print(array)

main()