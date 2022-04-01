import numpy as np
import time
import csv

#From: https://www.geeksforgeeks.org/insertion-sort/

def insertion_sort(array):
    # Loop from the second element of the array until
    # element at the end of the array
    for i in range(1, len(array)):
        # Specify the element of interest
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # If key_item is smaller than the number before it, 
        # run through the list of items and find the correct position
        while j >= 0 and array[j] > key_item:
            # Move the value one position to the left
            # and reposition j to point to the next element
            array[j + 1] = array[j]
            j -= 1

        # When the elements are shifted, move
        # `key_item` to its correct location
        array[j + 1] = key_item

    return array

def bucket_sort(input_list):
    # Find maximum value in the list and use length of 
    # the list to determine which value in the list goes into which bucket 
    max_value = max(input_list)
    size = max_value/len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # Call insertion sort on the elements of each bucket
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    # Join the sorted buckets into a single list
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

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
        bucket_sort(rng.integers(low=0, high=10, size=x))
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