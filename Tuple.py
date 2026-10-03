import numpy as np
#arr = np.array((1,2,3,4,5)) #[1 2 3 4 5]
d= np.array([1,2,3,4,5]) #[1 2 3 4 5]    #2D array
c= np.array([[1,2,3],[4,5,6]]) #[[1 2 3] [4 5 6]
b= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3E array
a= np.array(42)    #42       # 0 dimensional array 
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#When the array is created, you can define the number of dimensions by using the ndmin argument
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.