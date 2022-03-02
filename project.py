import numpy as np


rng = np.random.default_rng()
list= rng.integers(low=0, high=10, size=50)


# From: https://stackabuse.com/bubble-sort-in-python/
def bubble_sort(our_list):
    # Go through the array as many times as there are elements in the array
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

bubble_sort(list)
print(list)
