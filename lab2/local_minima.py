
def local_min(arr,n):
    min = []
    for i in range(0,n):
        if i==0:
            if arr[0]<arr[1]:
                min.append(arr[0])
        elif i!=n and (arr[i]<arr[i-1] and arr[i]<arr[i+1]) :
            min.append(arr[i])
        elif i==n : 
            if arr[n]<arr[n-1]:
                min.append(arr[n])
    return min


def main():
    arr = []
    n = int(input("Number of elements in array? "))
    print("Enter elements: ")
    for i in range(n):
        a = int(input())
        arr.append(a)
    mini = local_min(arr,n)
    print(f"Local minimas in array is : {mini}")

main()