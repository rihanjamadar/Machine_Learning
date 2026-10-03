import numpy as np
arr = np.array([1 ,2, 3, 4,5])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[2]+arr[3])
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
ar = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(ar[0, 1, 2]) 

print('5th element on 2nd row: ', a[1, 4])
print('2nd element on 1st row: ',a[0,1])