#binary Search

a = list(map(int, input("Enter sorted array: ").split()))
n = int(input("Enter searching number: "))

low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if a[mid] == n:
        print("Search Successful!")
        found = True
        break
    elif a[mid] < n:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Number not found!")
