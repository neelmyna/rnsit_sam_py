import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('IPLData.csv')


# Get top 5 run scorers
top_run_scorers = df[['Player Name', 'Team', 'Runs']].sort_values(by='Runs', ascending=False).head(5)
print(top_run_scorers)

# Plot top 5 run scorers
plt.figure(figsize=(8,5))
sns.barplot(data=top_run_scorers, x="Runs", y="Player Name", palette="viridis")
plt.xlabel("Total Runs")
plt.ylabel("Player Name")
plt.title("Top 5 Run Scorers in IPL")
plt.show()