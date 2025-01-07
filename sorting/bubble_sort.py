#Bubble Sort

a = list(map(int, input("Enter array : ").split()))
for n in range(len(a) - 1):
    for i in range(len(a) - 1 - n):
        if a[i] > a[i + 1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
print(f"Sorted array: {a}")
