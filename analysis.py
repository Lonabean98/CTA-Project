import pandas as pd
import matplotlib.pyplot as plt

# read in the csv file to a pandas dataframe
df = pd.read_csv('times.csv', header= None)

# rename column headings
df.columns = ['100', '200', '500','750', '1000', '1250','2500', '3750', '5000', '6250', '7500', '8750', '10000']

# round df values to 4 decimal places
df.round(4)

df= df.rename(index={0: 'Bubble Sort', 1: 'Merge Sort', 2: 'Bucket Sort', 3:'Quick Sort', 4: 'TimSort'})


df.index.name='Size'

#print(df.T) 

# switch columns and index
df.T.plot()
# set y axis limit
plt.ylim([0, 0.5])

plt.xlabel("Input size n")
plt.ylabel("Running time (milliseconds)")


plt.show()

