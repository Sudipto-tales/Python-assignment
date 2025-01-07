#Bubble Sort

a = list(map(int, input("Enter array : ").split()))
for pass_num in range(len(a) - 1):
    for i in range(len(a) - 1 - pass_num):
        if a[i] > a[i + 1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
print(f"Sorted array: {a}")
