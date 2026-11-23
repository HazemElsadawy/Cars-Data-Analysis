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
