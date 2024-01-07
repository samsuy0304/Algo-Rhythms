import sys
import numpy as np
import os

import sys
sys.path.append("..")

from RandomNumber_Generator.Random import Random
#################
# MySort class
#################
# class to sort lists of objects in different ways
class MySort:
    """A Basic sorting class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.m_random = Random(seed)

    # sorts array using bubble sort
    def BubbleSort(self, array):
        n = len(array)

        for i in range(n):
            # Each iteration brings in hope...
            already_sorted = True

            # Compare the neigbors.
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    array[j], array[j + 1] = array[j + 1], array[j]

                    # ... and that hope is taken away...
                    already_sorted = False

            # ... but peace is found.
            if already_sorted:
                break

        return array

    # sorts array using insertion sort
    def InsertionSort(self, array):
        # Loop from the second element of the array until last element
        for i in range(1, len(array)):
            # The chosen one has risen...
            key_item = array[i]

            # Chosen one begets others
            j = i - 1

            # Others find their way home
            while j >= 0 and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1

            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            array[j + 1] = key_item

        return array

    # sorts array using quicksort
    def QuickSort(self, array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        low, same, high = [], [], []

        # Select your `pivot` element randomly
        pivot = array[int(self.m_random.rand()*len(array))]

        for item in array:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
        return self.QuickSort(low) + same + self.QuickSort(high)

    # sorts array using default Python sort
    def DefaultSort(self, array):
        array.sort()

    def SelectionSort(self, array):
        n = len(array)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]
        return array

        
    
