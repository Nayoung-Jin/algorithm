num_tree, take_tree = map(int, input().split())
high_tree_list = list(map(int, input().split()))
start, end = 1, max(high_tree_list)

while start <= end:
    mid = (start + end)//2 
    get_tree = 0
    
    for i in high_tree_list:
        if i >= mid:
            get_tree += i - mid
    if get_tree >= take_tree:
        start = mid + 1
    else:
        end = mid - 1
print(end)