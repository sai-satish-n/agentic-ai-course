# Numpy

NumPy’s main object is the homogeneous multidimensional array.

It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers.

In NumPy dimensions are called axes.

**Example**
- [1, 2, 1], has one axis, and has 3 elements in it. So length of the axis is 3.
- [[1., 0., 0.], [0., 1., 2.]] the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.

NumPy’s array class is called **ndarray**


## ndarray attributes

- **ndarray.ndim**: the number of axes (dimensions) of the array
- **ndarray.shape**: the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. 
- **ndarray.size**: the total number of elements of the array. This is equal to the product of the elements of **shape**.
- **ndarray.dtype**: an object describing the type of the elements in the array. 
    - NumPy provides additional types of its own.
    - numpy.int32, numpy.int16, and numpy.float64 are some examples.

- **ndarray.itemsize**: the size in bytes of each element of the array
    - an array of elements of type float64 has itemsize 8 (=64/8).
    - an array of elements of type complex32 has itemsize 4 (=32/8).
    - it is equivalent to ndarray.dtype.itemsize

- **ndarray.data**: the buffer containing the actual elements of the array.


## Numpy Array Creation

### From Arrays and Tuples:
- You can create an array from a regular Python list or tuple using the array function.
- The type of the resulting array is deduced from the type of the elements in the sequences.

    ```
    a = np.array([1.2, 3.5, 5.1])
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    ```
- The type of the array can also be explicitly specified at creation time:

    ```c = np.array([[1, 2], [3, 4]], dtype=complex)```

Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.


### Creating with default values

- The function zeros creates an array full of zeros, 
- The function ones creates an array full of ones, and 
- The function empty creates an array whose initial content is random and depends on the state of the memory. 

**By default, the dtype of the created array is float64, but it can be specified via the key word argument dtype**

```
np.zeros((3, 4))
np.ones((2, 3, 4), dtype=np.int16)
np.empty((2, 3))
```

### Creating Sequences using Numpy

- To create sequences of numbers, NumPy provides the arange function
```
syntax: np.arange(start, end, step)
np.arange(0, 2, 0.3)
```
- When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. 
- For this reason, it is usually better to use the function **linspace** that receives as an argument the number of elements that we want, instead of the step
```
syntax: np.linspace(start, end, required_number_of_intervals)
np.linspace(0, 2, 9) 
```

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
- the last axis is printed from left to right,
- the second-to-last is printed from top to bottom,
- the rest are also printed from top to bottom, with each slice separated from the next by an empty line

One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.

```print(nd_array_var_name)```

- If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners.
- To disable this behaviour and force NumPy to print the entire array, you can change the printing options using **set_printoptions**.

```
>>> print(np.arange(10000).reshape(100, 100))
[[   0    1    2 ...   97   98   99]
 [ 100  101  102 ...  197  198  199]
 [ 200  201  202 ...  297  298  299]
 ...
 [9700 9701 9702 ... 9797 9798 9799]
 [9800 9801 9802 ... 9897 9898 9899]
 [9900 9901 9902 ... 9997 9998 9999]]

>>> np.set_printoptions(threshold=sys.maxsize)
```


### Creating Random Valued Arrays

```
rg = np.random.default_rng(1) # create instance of default random number generator.

b = rg.random((2, 3))
```

## Basic Numpy Operations:

- Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
```
>>> a = np.array([20, 30, 40, 50])
>>> b = np.arange(4)
>>> b
array([0, 1, 2, 3])
>>> c = a - b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10 * np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a < 35
array([ True,  True, False, False])
```

- The product operator `*` operates elementwise in NumPy arrays. 
- The matrix product can be performed using the `@` operator or the dot function or method

```
>>> A = np.array([[1, 1],
              [0, 1]])
>>> B = np.array([[2, 0],
              [3, 4]])
>>> A * B     # elementwise product
array([[2, 0],
       [0, 4]])
>>> A @ B     # matrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)  # another matrix product
array([[5, 4],
       [3, 4]])
```


**Some operations, such as `+=` and `*=`, act in place to modify an existing array rather than create a new one**



**When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as `upcasting`).**

Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the ndarray class
- sum()
- max()
- min()
- cumsum() cummulative sum(need to specify the axis)

By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the axis parameter you can apply an operation along the specified axis of an array.

```
>>> b = np.arange(12).reshape(3, 4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

>>> b.sum(axis=0)     # sum of each column
array([12, 15, 18, 21])

>>> b.min(axis=1)     # min of each row
array([0, 4, 8])

>>> b.cumsum(axis=1)  # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])

```


### Universal Functions
NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.

- exp(): raise the elements to power of e.
- sqrt()
- sin()
- cos()


```
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([1.        , 2.71828183, 7.3890561 ])
>>> np.sqrt(B)
array([0.        , 1.        , 1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([2., 0., 6.])
```

## Indexing, slicing and iterating
One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.

```
>>> a = np.arange(10)**3
>>> a[2]
>>> a[2:5]
>>> a[:6:2] = 1000 # from start to position 6, exclusive, set every 2nd element to 1000
>>> a[::-1] # reverse of a
>>> for i in a:
        print(i**(1 / 3.))
```