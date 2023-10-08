import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

url="https://danielperez.pythonanywhere.com/get_past_peeks/"
resp = requests.get(url)

df = pd.DataFrame(resp.json()["DataFrame"].values(),index=resp.json()["DataFrame"].keys())

time = np.array(resp.json()['time'])
lista = np.array(df)
value = np.array(lista[time])

plt.plot(lista)
plt.plot(time, value[time], "o")
plt.show()
value[time].shape
#df_raw.describe()
value[time].mean()
