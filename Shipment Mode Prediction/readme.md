# Shipment Mode Prediction

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
In today’s fast-paced logistics and e-commerce industry, choosing the right shipment mode is crucial for ensuring timely delivery and cost efficiency. 
This project focuses on predicting the most suitable shipment mode (such as air, road, or sea) based on various factors like weight, vendor, product type, and cost.

By using machine learning, the system analyzes historical shipping data to identify patterns and make accurate predictions. 
This helps businesses optimize their logistics operations, reduce delays, and improve customer satisfaction.

## Data

## Libraries
Python - Numpy, pandas, Seaborn, Matplotlib, Sklearn

## Methodology

### Exploratory Data Analysis
* Performed exploratory data analysis (EDA) to understand data distributions, analyze feature correlations, and identify potential outliers.
* Selected relevant features for predicting shipment mode.

### Feature Engineering
* Built a feature engineering pipeline to encode categorical variables, and apply feature scaling.
* Integrated the pipeline into the model training workflow to ensure consistent preprocessing across train–test split data before model training and evaluation.

### Model Training
* Trained multiple regression models including Logistic Regression, Decision Tree, Random Forest, and XGBoost to predict shipment mode.
* Evaluated model performance using accuracy, precision, recall and f1 scores.

### MLflow Tracking & Hyperparameter Tuning
* Logged models, hyperparameters, and performance metrics using MLflow for experiment tracking and reproducibility.
* Evaluated multiple models and selected the best-performing one based on precision score.
* Loaded the registered model and performed hyperparameter tuning using GridSearchCV.
* Registered the final model with the best hyperparameters in the MLflow.
  
<img width="1920" height="592" alt="image" src="https://github.com/user-attachments/assets/28c9f838-4f66-4905-be08-e4d7612991f0" />

<img width="1920" height="319" alt="image" src="https://github.com/user-attachments/assets/be0ff449-3fde-407e-b7c9-806ceede5aeb" />

