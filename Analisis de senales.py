import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import requests

url="https://danielperez.pythonanywhere.com/get_past_peeks/"
resp = requests.get(url)(data_to_find, height=3.88, distance=20)

df = pd.DataFrame(resp.json()["DataFrame"].values(),index=resp.json()["DataFrame"].keys())
time = np.array(resp.json()['time'])
lista = np.array(df)
value = np.array(lista[time])

#print(len(peaks[0]))
#plot Bz and peaks
plt.plot(lista)
plt.plot(time, value, "o")
plt.show()
value.shape
#df_raw.describe()
value.mean()
