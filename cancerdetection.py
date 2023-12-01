import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('/content/data.csv')
train.head()
df = pd.read_csv("data.csv")
print(df.head())
df['radius_mean'].plot(kind='hist')
sns.distplot(df['radius_mean'])
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='cubehelix'
sns.displot(train, x="radius_mean", element="step", kde=True))