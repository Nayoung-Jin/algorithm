def binarysearch(l1, n, first, last):
    if first > last:
        return False
    
    mid = (first + last) // 2
    if l1[mid] > n:
        return binarysearch(l1, n, first, mid - 1)
    elif l1[mid] < n:
        return binarysearch(l1, n, mid + 1, last)
    else:
        return True

num = int(input())
list1 = list(map(int, input().split()))
list1 = sorted(list1)
num2 = int(input())
list2 = list(map(int, input().split()))

for n in list2:
    if binarysearch(list1, n, 0, num - 1):
        print(1)
    else:
        print(0)