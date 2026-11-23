# Cars-Data-Analysis
EDA and visualization project in Python on the Kaggle Car Features and MSRP dataset (11,914 rows, 16 columns) covering cleaning, brands, HP vs MSRP, transmission shares, and price trends since 2000.
# 🚗 Data Analysis & Visualization About Cars Dataset


An exploratory data analysis (EDA) and data visualization project built in Python using the **Car Features and MSRP** dataset from Kaggle (`11,914` initial records and `16` columns)[cite: 5, 11]. The project examines vehicle distributions, engine horsepower vs. retail price (`MSRP`), transmission shares, and multi-year price trends[cite: 5, 8, 9, 10, 11].

## 📌 Project Overview
This project explores automotive specifications and pricing across **16 features** (`Make`, `Model`, `Year`, `Engine Fuel Type`, `Engine HP`, `Engine Cylinders`, `Transmission Type`, `Driven_Wheels`, `Number of Doors`, `Market Category`, `Vehicle Size`, `Vehicle Style`, `highway MPG`, `city mpg`, `Popularity`, and `MSRP`) to answer four core questions[cite: 5, 11]:
1. **Top Car Brands:** What are the 10 most frequent car makes in the dataset[cite: 5, 8, 11]?
2. **Horsepower vs. Price:** Is there a positive relationship between engine horsepower (`Engine HP`) and car price (`MSRP`)[cite: 5, 9, 11]?
3. **Transmission Distribution:** How are transmission types distributed across the dataset?
4. **Price Trend Over Time:** How has the average car price (`MSRP`) evolved since `2000`[cite: 5, 10, 11]?

## 📂 Repository Structure
```text
├── Cars.csv                 # Raw dataset (11,914 rows × 16 columns)
├── main.py                  # Data cleaning, EDA, and visualization script
├── Cars Data Analysis.pdf   # Project presentation & findings report
└── README.md                # Project documentation

## 🛠️ Tools & Technologies
- **Language:** Python[cite: 11]
- **Data Manipulation & Cleaning:** `pandas`, `numpy`[cite: 11]
- **Data Visualization:** `matplotlib`, `seaborn`[cite: 11]
- **Presentation / Report:** `Cars Data Analysis.pdf`[cite: 4]

## 🔄 Data Cleaning & Preprocessing (`main.py`)
- **Initial Inspection:** Loaded `Cars.csv` (`11,914` rows and `16` columns) and inspected data types, summary statistics, missing values, and exact duplicate records (`715` duplicates)[cite: 6, 7, 11].
- **Missing Values:** Dropped rows with missing entries in `Engine HP`, `Engine Cylinders`, and `Number of Doors`, and filled missing values in `Market Category` with `'Unknown'`[cite: 7, 11].
- **Deduplication & Data Types:** Removed duplicate rows (`df.drop_duplicates(inplace=True)`) and cast `Year` to `int` for chronological filtering (`Year >= 2000`)[cite: 7, 11].

## 📊 Key Findings
- **Top 10 Car Brands:** High-volume consumer brands such as **Chevrolet** and **Ford** lead the dataset, reflecting broad everyday vehicle representation[cite: 8, 11].
- **Engine HP vs. MSRP:** There is a positive correlation between `Engine HP` and `MSRP`, with prices rising sharply at higher horsepower levels typical of performance and luxury models[cite: 9, 11].
- **Transmission Types:** **Automatic** transmission makes up the largest share of vehicles, followed by **Manual**, while **Automated Manual** and **Direct Drive** represent smaller shares[cite: 9, 11].
- **Price Trend Since 2000:** Average `MSRP` for vehicles from `2000` onward shows an overall upward trend over time alongside evolving features and powertrains[cite: 10, 11].
