import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from eslearn.visualization.el_violine import ViolinPlotMatplotlib

data = pd.read_excel("./violin_demo_data.xlsx")
var_name = list(data.columns)

data_list = list(data.values.T)
plt.figure(figsize=(5,5))
ViolinPlotMatplotlib().plot(data_list, positions=np.arange(0,len(data_list)), facecolor=['r', 'g', 'b'])
plt.xticks(np.arange(0,len(data_list)), var_name, rotation=45)
plt.tight_layout()
plt.savefig("violin.pdf")