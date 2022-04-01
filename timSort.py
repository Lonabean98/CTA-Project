from random import randint
import numpy as np
import time
import csv

#From: https://www.geeksforgeeks.org/timsort/


MIN_MERGE = 32

def calcMinRun(n):
	"""Returns the minimum length of a
	run from 23 - 64 so that
	the len(array)/minrun is less than or
	equal to a power of 2.

	e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
	..., 127=>64, 128=>32, ...
	"""
	r = 0
	while n >= MIN_MERGE:
		r |= n & 1
		n >>= 1
	return n + r


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
	for i in range(left + 1, right + 1):
		j = i
		while j > left and arr[j] < arr[j - 1]:
			arr[j], arr[j - 1] = arr[j - 1], arr[j]
			j -= 1


# This function merges the sorted runs
def merge(arr, l, m, r):
	
	# original array is split into left and right parts
	len1, len2 = m - l + 1, r - m
	left, right = [], []
	for i in range(0, len1):
		left.append(arr[l + i])
	for i in range(0, len2):
		right.append(arr[m + 1 + i])

	i, j, k = 0, 0, l
	
	# after comparing, join these two sub 
	# arrays into larger sub array
	while i < len1 and j < len2:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1

		else:
			arr[k] = right[j]
			j += 1

		k += 1

	# Copy remaining elements of left, if any
	while i < len1:
		arr[k] = left[i]
		k += 1
		i += 1

	# Copy remaining element of right, if any
	while j < len2:
		arr[k] = right[j]
		k += 1
		j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr):
	n = len(arr)
	minRun = calcMinRun(n)
	
	# Sort individual subarrays of size RUN
	for start in range(0, n, minRun):
		end = min(start + minRun - 1, n - 1)
		insertionSort(arr, start, end)

	# Start merging from size RUN (or 32). It will merge
	# to form size 64, then 128, 256 and so on ....
	size = minRun
	while size < n:
		
		# Pick starting point of left sub array. We
		# are going to merge arr[left..left+size-1]
		# and arr[left+size, left+2*size-1]
		# After every merge, we increase left by 2*size
		for left in range(0, n, 2 * size):

			# Find ending point of left sub array
			# mid+1 is starting point of right sub array
			mid = min(n - 1, left + size - 1)
			right = min((left + 2 * size - 1), (n - 1))

			# Merge sub array arr[left.....mid] &
			# arr[mid+1....right]
			if mid < right:
				merge(arr, left, mid, right)

		size = 2 * size



# Initialise the random generator
rng = np.random.default_rng()

# empty array to contain sorting times
test= []
# Function to allow multiple input instances 
def runs(noRuns):
    # Loop through list of input sizes
    for x in noRuns:
        # fetches current number of seconds since epoch
        start_time = time.time()
        # call the sorting function
        timSort(rng.integers(low=0, high=10, size=x))
        # fetches current number of seconds since epoch
        end_time = time.time()
        # subtract start and end times to get the elapsed time
        time_elapsed = end_time - start_time
        # add this time to the array
        test.append(time_elapsed)
    


# Run the test 10 times
for x in range(10): 
    runs([100, 200, 500,750, 1000, 1250,2500, 3750, 5000, 6250, 7500, 8750, 10000])

# reshape the array to 2 dimensions
test= np.reshape(test, (10, 13))


# print mean of columns
print(test.mean(axis=0))

# Open the times.csv file and append what comes next
with open('times.csv', 'a') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(test.mean(axis=0))