import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Cars.csv')

# 2. Dataset Overview
print(df.head())
print(df.shape)
print(df.dtypes)
print("\n--- Summary Statistics ---")
print(df.describe(include="all"))
print("\n--- Missing Values Count ---")
print(df.isnull().sum())

df.dropna(subset=['Engine HP', 'Engine Cylinders', 'Number of Doors'], inplace=True)
df['Market Category'].fillna('Unknown', inplace=True)

# 4. Duplicate Values
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)
print("\nData after remove Duplicates")
print(df.shape)

# 5. Data Type Correction
df['Year'] = df['Year'].astype(int)


plt.figure(figsize=(10, 6))
top_makes = df['Make'].value_counts().head(10)
top_makes.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Car Brands')
plt.xlabel('Car Brande')
plt.ylabel('Count of Cars')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Q2: Engine HP vs MSRP (Scatter Plot)
plt.figure(figsize=(10, 6))
plt.scatter(df['Engine HP'], df['MSRP'], alpha=0.5, color="coral")
plt.title('Relationship Between Engine HP and MSRP')
plt.xlabel('Engine Power (HP)')
plt.ylabel('Price in USD')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Q3: Transmission Type Distribution (Pie Chart)

sns.set_theme(style="whitegrid")


trans_counts = df['Transmission Type'].value_counts().head(4)
colors = ['#4F81BD', '#C0504D', '#9BBB59', '#8064A2']
explode = (0.05, 0, 0, 0)  
fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    trans_counts, 
    explode=explode, 
    labels=trans_counts.index, 
    autopct='%1.1f%%',
    startangle=140, 
    colors=colors,
    textprops=dict(color="black", fontsize=12, weight="bold"), 
    pctdistance=0.75,
    wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2) 
)


for autotext in autotexts:
    autotext.set_color('white') 
    autotext.set_fontsize(13)


plt.title(
    "Distribution of Transmission Types", 
    fontsize=16, 
    weight='bold', 
    pad=20, 
    color='#333333'
)

plt.ylabel('')

plt.legend(
    wedges, 
    trans_counts.index,
    title="Transmission Types",
    loc="center left",
    bbox_to_anchor=(1, 0, 0, 1), 
    fontsize=11
)


plt.tight_layout()
plt.show()

# Q4: Price Trend Over the Years (Line Chart)
plt.figure(figsize=(10, 6))
modern = df[df['Year'] >= 2000]
price_year = modern.groupby('Year')['MSRP'].mean()
plt.plot(price_year.index, price_year.values, marker="o", color='lightblue', linewidth=2)
plt.title('Average Car Price Trend Since 2000')
plt.xlabel('Year of Manufacture')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()