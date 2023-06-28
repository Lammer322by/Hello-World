import pandas
import matplotlib.pyplot as plt
from scipy.stats import kstest

data = pandas.read_csv("important_data.csv")

data['summ'] = data['dice1'] + data['dice2']


print(kstest(data['summ'], 'norm'))

graph = pandas.DataFrame(data={'Summ': data['summ']})
graph.plot.kde()
plt.show()
