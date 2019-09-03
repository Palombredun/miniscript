def merge_sort(array): 
    if len(array) >1: 
        mid = len(array)//2 #Finding the mid of the array 
        L = array[:mid] # Dividing the array elements  
        R = array[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                array[k] = L[i] 
                i+=1
            else: 
                ay[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            array[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            array[k] = R[j] 
            j+=1
            k+=1

print(array)
merge_sort(array)
print(array)
