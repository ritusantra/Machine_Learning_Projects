# 🚢 PredictShip: One Stop Shipment Intelligence System

## Table of Content
* [Introduction](#introduction)
* [System Architecture](#system-architecture)
* [Data](#data)
* [Libraries](#libraries)
* [Methodology](#methodology)
     * [Exploratory Data Analysis](#exploratory-data-analysis)
     * [Feature Engineering](#feature-engineering)
     * [Model Training](#model-training)
     * [MLflow Tracking](#mlflow-tracking)
 

## Introduction
In today’s high-speed logistics and e-commerce landscape, every shipment decision directly impacts cost, efficiency, and risk. **PredictShip: Shipment Intelligence System** is a powerful, ML-driven solution designed to bring intelligence to two critical areas: shipment planning and insurance valuation.

By leveraging machine learning models, PredictShip predicts the optimal shipment mode while simultaneously determining the precise insurance amount required for each shipment. Using key inputs such as weight, pricing, product type, vendor, cost, and shipment value, the system transforms raw data into actionable insights.

The impact is reduced logistics costs, minimized financial risk, elimination of over- or under-insurance, and faster, smarter operations. This solution empowers businesses to move from reactive decision-making to proactive, and delivering a more reliable customer experience.

## Data


## System Architecture

PredictShip is designed as a modular, end-to-end machine learning system built with an interactive Streamlit-based frontend and robust backend pipelines for prediction and model management.

At the user interface layer, the system is developed using Streamlit, where users can seamlessly switch between two modules:

1. Shipment Mode Prediction
2. Shipment Insurance Cost Prediction

This modular design ensures flexibility, allowing users to select their desired prediction task and input relevant shipment details through an intuitive interface.

### Backend Architecture

**1. Feature Engineering Pipeline**

For both modules, a dedicated feature engineering pipeline is implemented to preprocess raw input data. This includes:

* Data cleaning
* Encoding categorical variables
* Feature transformation and scaling

These pipelines are saved and reused during inference to maintain consistency between training and streamlit development.

**2. Model Training & Selection**

Each module follows a structured ML workflow:

**Shipment Mode Prediction Module**

* Models trained: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost
* Performance evaluated using classification metrics - Precision, Recall, F1 score, Accuracy
* XGBoost selected as the final model based on best performance across all the metrics especially Precision 

**Shipment Insurance Cost Prediction Module**

* Models trained: Linear Regression, Decision Tree, XGBoost
* Evaluated using regression metrics - MAE, MSE, RMSE, R2 score, Adjusted R2 score
* XGBoost selected as the final model due to low error metrics and higher Adjusted R2 score

**3. Experiment Tracking with MLflow**

To ensure reproducibility and efficient experimentation:

* MLflow is used to track model performance
* Hyperparameter tuning and metrics are logged
* Best-performing models are identified and versioned

### Deployment & Integration Layer
* Final feature engineering pipelines and trained XGBoost models are serialized as .pkl files
* These artifacts are integrated into the Streamlit application
* When a user provides input, data flows through:
    * Feature engineering pipeline
    * Selected trained model
    * Prediction output displayed

### End-to-End Flow

User Input → Streamlit UI → Module Selection → Feature Engineering Pipeline → Trained XGBoost Model → Prediction Output

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
* Loaded the registered model and performed hyperparameter tuning using GridSearchCV/RandomizedSearchCV.
* Registered the final model with the best hyperparameters in the MLflow.

