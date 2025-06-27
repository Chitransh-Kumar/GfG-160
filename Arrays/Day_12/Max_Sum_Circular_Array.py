def max_sum_circular_array(arr):
    n=len(arr)
    global_max=arr[0]
    global_min=arr[0]

    current_max=0
    current_min=0
    total_sum=0

    for i in range(n):
        total_sum=total_sum+arr[i]

    for i in range(n):
        current_max=max(current_max+arr[i],arr[i])
        global_max=max(global_max,current_max)

    for i in range(n):
        current_min=min(current_min+arr[i],arr[i])
        global_min=min(global_min,current_min)

    if global_max<0:
        return global_max
    else:
        return max(global_max,total_sum-global_min)

arr=[10,-3,-4,7,6,5,-4,-1]
print(max_sum_circular_array(arr))
