import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv('titanic.csv')

print("First 10 rows:")
print(df.head(10))

# Bar Chart: Distribution of Gender 
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', data=df)
plt.title("Distribution of Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Histogram: Distribution of Age
plt.figure(figsize=(8,5))
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
