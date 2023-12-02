import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your cancer detection dataset
plt.figure(figsize=(8, 6))
sns.histplot(df['smoothness_worst'], bins='auto', kde=True, color='blue')
plt.xlabel('smoothness_worst')
plt.ylabel('Frequency')
plt.title('Distribution of Tumor Sizes')
plt.show()
