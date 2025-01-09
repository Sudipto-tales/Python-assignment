#recursive binary Search

a = list(map(int, input("Enter sorted array: ").split()))
n = int(input("Enter searching number: "))
low = 0
high = len(a) - 1

def binary_search(a,n,low,high):
    if low > high:
      return False
    mid = (low + high) // 2
    if a[mid] == n:
       return True
    elif a[mid] < n:
        return binary_search(a,n,mid + 1,high)
    else:
        return binary_search(a,n,low,mid - 1)

if binary_search(a, n, low, high):
    print("Search Successful!")
else:
    print("Number not found!")
