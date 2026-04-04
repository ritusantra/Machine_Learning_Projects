# 🚢 PredictShip: One Stop Shipment Intelligence System

## Table of Content
* [Introduction](#introduction)
* [System Architecture](#system-architecture)
* [Data](#data)
* [Tech Stack](#tech-stack)
* [Images](#images)
* [Repository Structure](#repository-structure)
 

## Introduction
In today’s high-speed logistics and e-commerce landscape, every shipment decision directly impacts cost, efficiency, and risk. **PredictShip: Shipment Intelligence System** is a powerful, ML-driven solution designed to bring intelligence to two critical areas: shipment planning and insurance valuation.

By leveraging machine learning models, PredictShip predicts the optimal shipment mode while simultaneously determining the precise insurance amount required for each shipment. Using key inputs such as weight, pricing, product type, vendor, cost, and shipment value, the system transforms raw data into actionable insights.

The impact is reduced logistics costs, minimized financial risk, elimination of over- or under-insurance, and faster, smarter operations. This solution empowers businesses to move from reactive decision-making to proactive, and delivering a more reliable customer experience.

## Data

| Column                         | Description                                               |
| ------------------------------ | --------------------------------------------------------- |
| `ID`                           | Unique identifier for each shipment record                |
| `Project Code`                 | Project under which the shipment is categorized           |
| `PQ #`                         | Pre-Qualification reference/status                        |
| `PO / SO #`                    | Purchase Order or Sales Order number                      |
| `ASN/DN #`                     | Advanced Shipping Notice or Delivery Note number          |
| `Country`                      | Destination country of the shipment                       |
| `Managed By`                   | Entity managing the shipment                              |
| `Fulfill Via`                  | Fulfillment method (e.g., Direct Drop)                    |
| `Vendor INCO Term`             | International shipping terms (EXW, FCA, CIP, etc.)        |
| `Shipment Mode`                | Mode of transport (Air, Sea, Truck) **(Target - Model 1)** |
| `PQ First Sent to Client Date` | Date when PQ was first shared with client                 |
| `PO Sent to Vendor Date`       | Date when PO was sent to vendor                           |
| `Scheduled Delivery Date`      | Planned delivery date                                     |
| `Delivered to Client Date`     | Actual delivery date                                      |
| `Delivery Recorded Date`       | Date when delivery was recorded                           |
| `Product Group`                | Category of product (e.g., ARV, HRDT)                     |
| `Sub Classification`           | Sub-category (Adult, Pediatric, HIV test, etc.)           |
| `Vendor`                       | Supplier or manufacturer                                  |
| `Item Description`             | Detailed product description                              |
| `Molecule/Test Type`           | Drug molecule or test type                                |
| `Brand`                        | Brand name                                                |
| `Dosage`                       | Drug strength/specification                               |
| `Dosage Form`                  | Form (Tablet, Capsule, Solution, etc.)                    |
| `Unit of Measure (Per Pack)`   | Units per pack                                            |
| `Line Item Quantity`           | Quantity ordered                                          |
| `Line Item Value`              | Total value of items                                      |
| `Pack Price`                   | Price per pack                                            |
| `Unit Price`                   | Price per unit                                            |
| `Manufacturing Site`           | Production location                                       |
| `First Line Designation`       | Indicates first-line treatment (Yes/No)                   |
| `Weight (Kilograms)`           | Shipment weight                                           |
| `Freight Cost (USD)`           | Transportation cost                                       |
| `Line Item Insurance (USD)`    | Insurance amount **(Target - Model 2)**                   |



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

## Tech Stack
* Python - Numpy, pandas, Seaborn, Matplotlib, Sklearn
* MLflow
* Streamlit

## Images

![Capturesssss](https://github.com/user-attachments/assets/cefdd717-84eb-48ed-b271-9e300666b9f9)
![Capturesss](https://github.com/user-attachments/assets/97f9f6e6-a293-49f2-b4d7-48442db7c42e)


## Repository Structure
```
PredictShip: Shipment Intelligence System
│
├── Run
│   ├── app.py                          # Streamlit application entry point
│   ├── readme.md                      # Overview of Run folder contents
│   ├── requirements.txt               # Project dependencies
│   ├── shp_ins_model.pkl              # Trained shipment insurance model
│   ├── shp_ins_pipeline.pkl           # Feature engineering pipeline for insurance model
│   ├── shp_type_model.pkl             # Trained shipment mode prediction model
│   ├── shp_type_pipeline.pkl          # Feature engineering pipeline for shipment mode model
│
├── Shipment Insurance Prediction
│   ├── 01_Exploratory_Data_Analysis.ipynb   # Data exploration and visualization notebook
│   ├── 02_Feature_Engineering.ipynb         # Feature engineering steps notebook
│   ├── 03_Model_Training.ipynb               # Model training and evaluation notebook
│   ├── readme.md                             # Documentation specific to insurance prediction module
│
├── Shipment Mode Prediction
│   ├── 01_Exploratory_Data_Analysis.ipynb   # Data exploration and visualization notebook
│   ├── 02_Feature_Engineering.ipynb         # Feature engineering steps notebook
│   ├── 03_Model_Training.ipynb               # Model training and evaluation notebook
│   ├── readme.md                             # Documentation specific to shipment mode prediction module
│
└── readme.md                                # Main project README with overview and instructions

```
