
def shift_swap(a , b, array):
    temp = array[b]
    while b>a:
        array[b] = array[b-1]
        b = b-1
    array[a] = temp


def insertion_sort(n, array):
    j = 1
    while j<n:
        k = 0
        while k!=j:
            if array[k]<array[j]:
                k=k+1
            else: shift_swap(k,j,array)                   
        j=j+1
        

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
    insertion_sort(n, array)
    print(array)
    
main()