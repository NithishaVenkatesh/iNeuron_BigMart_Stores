# BigMart Sales Prediction

This project aims to predict sales for BigMart outlets using machine learning techniques, enabling better inventory management and sales strategies.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling Approach](#modeling-approach)
- [Results](#results)


---

## Project Overview

BigMart, a large retail chain, seeks to enhance its sales forecasting capabilities to improve inventory management and profitability. This project involves building a predictive model to estimate the sales of each product at different outlets. The model considers various factors, including product attributes and outlet characteristics, to make accurate predictions.

---

## Dataset

The dataset comprises sales data for 1,559 products across 10 different stores. It includes the following features:

- **Item_Identifier**: Unique product ID
- **Item_Weight**: Weight of the product
- **Item_Fat_Content**: Fat content of the product (e.g., Low Fat, Regular)
- **Item_Visibility**: The percentage of total display area allocated to the product in the store
- **Item_Type**: Category to which the product belongs
- **Item_MRP**: Maximum Retail Price of the product
- **Outlet_Identifier**: Unique store ID
- **Outlet_Establishment_Year**: Year the store was established
- **Outlet_Size**: Size of the store (e.g., Small, Medium, Large)
- **Outlet_Location_Type**: Type of city in which the store is located
- **Outlet_Type**: Type of outlet (e.g., Grocery Store, Supermarket)
- **Item_Outlet_Sales**: Sales of the product in the particular store (target variable)

The dataset is available on [Kaggle](https://www.kaggle.com/datasets/shivan118/big-mart-sales-prediction-datasets).

---

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NithishaVenkatesh/iNeuron_BigMart_Sales_Prediction.git
   cd iNeuron_BigMart_Sales_Prediction
   
2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt

---
## Usage

Ensure the dataset is in the project directory. If not, download it from the link provided above and place it appropriately.

Run the data preprocessing and model training script:

bash
python app.py

**For prediction**:
Load the trained model (BigMart_Model.pkl).
Prepare the input data in the required format.
Use the model's predict method to obtain sales predictions.

---

## Modeling Approach
The project follows these steps:

**Exploratory Data Analysis (EDA)**: Understanding data distributions, identifying missing values, and uncovering patterns.

**Data Preprocessing**: Handling missing values, encoding categorical variables, and feature scaling.

**Feature Engineering**: Creating new features based on existing data to enhance model performance.

**Model Selection**: Evaluating multiple regression algorithms, including Linear Regression, Random Forest Regressor, and XGBoost, to identify the best-performing model.

**Model Evaluation**: Assessing model performance using metrics such as RMSE (Root Mean Squared Error) and R² score.

**Hyperparameter Tuning**: Optimizing model parameters to improve accuracy.

---

## Results

The final model achieved the following performance metrics on the test set:

- **R² Score**: 0.87
