import numpy as np
import timeit
import time
import statistics
import numpy as np




# From: https://stackabuse.com/bubble-sort-in-python/

def bubble_sort(our_list):
    # Go through the array as many times as there are elements in the array
    for i in range(len(our_list)):
        # Go through the array up to the second last element
        for j in range(len(our_list) - 1):
            # If the element before the next element is larger...
            if our_list[j] > our_list[j+1]:
                # Swap their positions
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

rng = np.random.default_rng()
list= rng.integers(low=0, high=10, size=1000)


test= []
start_time = time . time ()
# call your function
bubble_sort(list)
end_time = time . time ()
time_elapsed = end_time - start_time

for i in range(10):
  test.append(time_elapsed)
print(round(np.mean(test), 3))
   