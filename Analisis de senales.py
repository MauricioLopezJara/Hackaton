import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

headers = ['year', 'day', 'hour', 'B_scalar','Bz_GSM','Bz_GSE','SW_temperature', 'SW_proton_density','Plasma_Speed','Flow_pressure']
df = pd.read_csv('data1.txt', delim_whitespace=' ',names=headers)
#Found max values for each column
df.max()
#Create list with max values of each column
max_values = [9999, 999, 99, 99, 99, 99, 9999999.00, 999.90, 9999.00, 99.99]
# Remove rows with missing values
df_raw = df[(df != max_values).all(axis=1)]

# reset index
df_raw = df_raw.reset_index(drop=True)

data_to_find = df_raw['Bz_GSM']

peaks = sp.signal.find_peaks(data_to_find, height=3.88, distance=20)
print(len(peaks[0]))
#plot Bz and peaks
plt.plot(data_to_find)
plt.plot(peaks[0], data_to_find[peaks[0]], "o")
plt.show()
data_to_find[peaks[0]].shape
df_raw.describe()
data_to_find[peaks[0]].mean()