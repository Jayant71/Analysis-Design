def fibo(n):
    i,a,b,s = 0,0,1,0
    l = [] 
    while i<n:
        l.append(s)
        a = b
        b = s
        s = a+b
        i=i+1
        
    return l

def main():
    n = int(input("Number of terms? "))
    print(fibo(n))

main()