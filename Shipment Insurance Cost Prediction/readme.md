# 💲🚢 Shipment Insurance Cost Prediction

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

## Data


## Libraries
Python - Numpy, pandas, Seaborn, Matplotlib, Sklearn

## Methodology

### Exploratory Data Analysis
* Performed exploratory data analysis (EDA) to understand data quality issues, data distributions, analyze feature correlations, and identify potential outliers.
* Selected relevant features for predicting shipment insurance costs - weight, pricing, and shipment mode.

### Feature Engineering
* Built a feature engineering pipeline to handle missing values, encode categorical variables, and apply feature scaling.
* Integrated the pipeline into the model training workflow to ensure consistent preprocessing across train–test split data before model training and evaluation.

### Model Training
* Trained multiple regression models including Linear Regression, Decision Tree, and XGBoost to predict shipment insurance costs.
* Evaluated model performance using MAE, MSE. RMSE, R2 score and adjusted R2 scores.
* Seletec XGBoost as the best model due to its high adjusted R2 score and lower error metrics.

### MLflow Tracking & Hyperparameter Tuning
* Logged models, hyperparameters, and performance metrics using MLflow for experiment tracking and reproducibility.
* Evaluated multiple models and selected the best-performing one based on precision score.
* Loaded the registered model and performed hyperparameter tuning using RandomizedSearchCV.
* Registered the final model with the best hyperparameters in the MLflow.

