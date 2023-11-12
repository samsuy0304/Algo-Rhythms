#Sorting Algorithms Module
## Description
The MySort module is a collection of sorting algorithms implemented in the MySort class. This module includes popular sorting algorithms such as Bubble Sort, Insertion Sort, Quicksort, and the default Python sort. Whether you need a simple sorting solution or a more advanced algorithm, this module has you covered.

##Usage
The MySort class provides a set of sorting algorithms that you can use in your Python projects. Here's an example of how to use the module:

```
# Import the MySort class
from mysort import MySort

# Create an instance of MySort
mysort_instance = MySort()

# Example list to sort
my_list = [4, 2, 7, 1, 9, 5]

# Use Bubble Sort to sort the list
sorted_list = mysort_instance.bubble_sort(my_list)

# Print the sorted list
print("Sorted List (Bubble Sort):", sorted_list)
Feel free to replace bubble_sort with other sorting methods such as insertion_sort, quick_sort, or use the default Python sort method:
```

## Avalaible Algorithms

### Bubble Sort
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

###Insertion Sort:
Insertion Sort is another straightforward algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort, but it performs well for small datasets or lists that are mostly sorted.

###Quicksort:
Quicksort is a highly efficient and widely used sorting algorithm. It uses a divide-and-conquer strategy to sort elements by selecting a 'pivot' element and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### Python Sort:
The default Python sorting algorithm, accessed using the sorted() function, is an implementation of Timsort. Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data and is the default sorting algorithm in Python's sorted() function and the sort() method of Python lists.
