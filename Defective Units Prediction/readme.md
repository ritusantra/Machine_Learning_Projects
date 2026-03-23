# Defective Units Prediction

## Table of Content
* [Introduction](#introduction)
* [Data](#data)
* [Libraries](#libraries)
* [Methodology](#methodology)
* [Exploratory Data Analysis](#data-cleansing-and-manipulation)
* [Feature Engineering](#dax-measures)
* [Model Training and Evaluation]()

## Introduction
Product quality is a critical factor in procurement and supply chain management. Receiving a high number of defective units from suppliers can lead to production disruptions, increased inspection costs, and delays in downstream operations. However, procurement teams often identify quality issues only after the goods are delivered, making it difficult to take preventive actions.

This project focuses on building a machine learning model to predict the number of defective units in a purchase order using historical procurement data. By analyzing factors such as supplier, item category, order quantity, and pricing details, the model estimates the expected number of defective units before the order is fulfilled. These predictions can help procurement teams identify high-risk orders, improve supplier evaluation, and take proactive quality control measures.
 
## Data
The [dataset](https://www.kaggle.com/datasets/shahriarkabir/procurement-kpi-analysis-dataset) contains historical purchase order records with supplier, pricing, and delivery information.

## Data Dictionary

| Feature | Description |
|--------|-------------|
| **PO_ID** | Unique identifier for each purchase order |
| **Supplier** | Name of the supplier providing the goods |
| **Order_Date** | Date on which the purchase order was placed |
| **Delivery_Date** | Date on which the goods were delivered |
| **Item_Category** | Category of the ordered product (e.g., raw materials, electronics, packaging) |
| **Quantity** | Total number of units ordered in the purchase order |
| **Unit_Price** | Original price per unit before negotiation |
| **Negotiated_Price** | Final price per unit after negotiation with the supplier |
| **Defective_Units** | Number of defective units identified |
| **Compliance** | Indicator showing whether the supplier complied with quality or procurement standards (Yes / No) |

## Libraries
Python - Numpy, pandas, Seaborn, Matplotlib, Sklearn

## Methodology
### Feature Creation
Created new features from the data:
* **Lead Time** = Delivery_Date - Order_Date
* **Price Ratio** = Negotiated_Price/Unit_Price
* **Negotiated vs Unit Price** = Unit_Price - Negotiated_Price

### Exploratory Data Analysis
Performed exploratory data analysis on the data to understand the underlying data distribution, correlation between features, and identify outliers.

### Feature Engineering
* Filled the missing values
* Capped outliers
* Encoding categorical values
* Transformed and scaled numerical features

### Model Training and Evaluation
* Trained multiple regression models including Linear Regression, Ridge Regression, Lasso Regression, and Decision Tree Regressor to predict the defective units.
* Evaluated model performance using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R² Score, and Adjusted R² Score.
* Compared the performance of all models and selected Linear Regression as the final model due to its higher Adjusted R² score and lower prediction error, indicating better generalization on the dataset.
 
 
 
