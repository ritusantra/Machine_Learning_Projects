# Defective Units Prediction From Purchase Orders

## Table of Content
* [Introduction](#introduction)
* [Data](#data)
* [Libraries](#libraries)
* [Methodology](#methodology)
     * [Features Creation](#features-creation)
     * [Exploratory Data Analysis](#exploratory-data-analysis)
     * [Feature Engineering](#feature-engineering)
     * [Model Training and Evaluation](#model-training-and-evaluation)
     * [API Endpoint](#api-endpoint)

## Introduction
Product quality is a critical factor in procurement and supply chain management. Receiving a high number of defective units from suppliers can lead to production disruptions, increased inspection costs, and delays in downstream operations. However, procurement teams often identify quality issues only after the goods are delivered, making it difficult to take preventive actions.

This project focuses on building a machine learning model to predict the number of defective units in a purchase order using historical procurement data. By analyzing factors such as supplier, item category, order quantity, and pricing details, the model estimates the expected number of defective units before the order is fulfilled. These predictions can help procurement teams identify high-risk orders, improve supplier evaluation, and take proactive quality control measures.
 
## Data
The [dataset](https://www.kaggle.com/datasets/shahriarkabir/procurement-kpi-analysis-dataset) contains historical purchase order records with supplier, pricing, and delivery information.

## Data Dictionary

| Features | Description |
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

### New Features Creation
Created new features from the data:
* **Lead Time** = Delivery_Date - Order_Date
* **Price Ratio** = Negotiated_Price/Unit_Price
* **Negotiated vs Unit Price** = Unit_Price - Negotiated_Price

### Exploratory Data Analysis
* Performed exploratory data analysis (EDA) to understand data distributions, analyze feature correlations, and identify potential outliers.
* Selected relevant features for predicting defective units by evaluating feature correlation and assessing multicollinearity among predictors.

### Feature Engineering
* Built a feature engineering pipeline to handle missing values, cap outliers, encode categorical variables, and apply Yeo–Johnson transformation and feature scaling.
* Integrated the pipeline into the model training workflow to ensure consistent preprocessing across train–test split data before model training and evaluation.

### Model Training and Evaluation
* Trained multiple regression models including Linear Regression, Ridge, Lasso, and Decision Tree Regressor to predict defective units.
* Evaluated model performance using MAE, MSE, RMSE, R², and Adjusted R².
* Selected Linear Regression as the final model due to its higher Adjusted R² and lower prediction errors.

 ### API Endpoint
* Depoyed and exposed the model through an API endpoint using FastAPI so anyone can send data and get predictions in real time.

 <img width="1861" height="854" alt="image" src="https://github.com/user-attachments/assets/2269873c-821f-4bc2-bcc5-d75d266b3953" />
 <img width="961" height="432" alt="image" src="https://github.com/user-attachments/assets/1dccb04f-4da3-4e00-8f8f-45aedaeb7fc2" />


 
 
