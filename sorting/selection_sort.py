#Selection Sort

a = list(map(int, input("Enter array : ").split()))
for n in range(len(a)):
    min = n
    for i in range(n + 1,len(a)):
        if a[i] < a[n]:
            min = i
    temp = a[n]        
    a[n] = a[min]    
    a[min] = temp
print(f"Sorted array: {a}")
