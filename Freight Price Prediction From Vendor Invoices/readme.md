# Freight Price Prediction From Vendor Invoices

## Table of Content
* [Introduction](#introduction)
* [Data](#data)
* [Libraries](#libraries)
* [Methodology](#methodology)
     * [Exploratory Data Analysis](#exploratory-data-analysis)
     * [Feature Engineering](#feature-engineering)
     * [Model Training](#model-training)
     * [MLflow Tracking](#mlflow-tracking)
 

## Introduction
Freight costs are a critical component of supply chain operations, often varying due to factors such as shipment value, quantity, and vendor pricing strategies. 
This project develops a machine learning model to predict freight charges using historical vendor invoice data, leveraging dollar price and quantity to estimate freight cost. 
The solution helps improve cost transparency and supports better decision-making in logistics.

## Data

## Libraries
Python - Numpy, pandas, Seaborn, Matplotlib, Sklearn

## Methodology

### Exploratory Data Analysis
* Performed exploratory data analysis (EDA) to understand data distributions, analyze feature correlations, and identify potential outliers.
* Selected relevant features for predicting defective units by evaluating feature correlation and assessing multicollinearity among features.

### Feature Engineering
* Built a feature engineering pipeline to encode categorical variables, and apply feature scaling.
* Integrated the pipeline into the model training workflow to ensure consistent preprocessing across train–test split data before model training and evaluation.

### Model Training
* Trained multiple regression models including Linear Regression, Ridge, Lasso, and Decision Tree Regressor to predict defective units.
* Evaluated model performance using MAE, MSE, RMSE, R², and Adjusted R².
* Selected Linear Regression as the final model due to its higher Adjusted R² and lower prediction errors.

### MLflow Tracking
* Logged models, hyperparameters, and performance metrics using MLflow for experiment tracking and reproducibility.
* Evaluated multiple models and selected the best-performing one based on Adjusted R² score.
* Promoted the top-performing model from challenger to production (champion) within the MLflow model registry.

<img width="1920" height="592" alt="image" src="https://github.com/user-attachments/assets/28c9f838-4f66-4905-be08-e4d7612991f0" />

<img width="1920" height="319" alt="image" src="https://github.com/user-attachments/assets/be0ff449-3fde-407e-b7c9-806ceede5aeb" />


