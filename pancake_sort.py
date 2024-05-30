def pancake_sort(arr):
  def flip(arr, k):
    left , right = 0, k # n-1
    while left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -=1
    return
  
  def getMaxIndex(arr, end_index):
    output = 0
    for i in range(end_index+1): # n
      if arr[i]>arr[output]:
        output = i
    return output
  
  def pancakeSort(arr):
    n = len(arr)
    for i in range(n):
      max_idx = getMaxIndex(arr, n-i-1) # i= 0 , n+1
      flip(arr, max_idx)
      flip(arr, n-i-1) # n-1
    return arr

  return pancakeSort(arr)
  

"""
arr = [1, 5, 4, 3, 2] o(n* (2n) o(n2)
max_ix = getMaxIndex(arr)
k = max_ix
      [5, 1, 4, 3, 2] o(n)
            [2,3,4, 1,5] o(n)
min = 1

flip(arr, 2)
 1,4,5
approach:



pancake_sort([])



arr = [1, 5, 4, 3, 2]

flip(arr, 3) -- reverse 3 first elt
[1, 5, 4] -> [4,5,1]
return None
approach:

l = 0 r=k-1

swap arr[0] arr[2]

l = 1  r=1

O(k)




"""
