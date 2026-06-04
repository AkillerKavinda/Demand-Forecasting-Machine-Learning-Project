# Demand Forecasting Machine Learning Project

This project is a Streamlit web app that predicts product demand using a machine learning regression model.

The app takes product-related inputs such as price, discount, inventory level, promotion status, competitor pricing, and product category. It then predicts the expected demand for the product.

## Project Overview

Demand forecasting helps businesses estimate how much of a product customers may buy. This can help with stock planning, pricing decisions, and reducing waste from overstocking.

In this project, an XGBoost regression model was trained to predict demand based on product and market features.

## Features

- Predicts product demand using a trained XGBoost model
- Simple Streamlit web interface
- User-friendly category selection
- Takes multiple input features:
  - Price
  - Discount
  - Inventory level
  - Promotion status
  - Competitor pricing
  - Product category

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Pickle

## Project Files

```text
Demand-Forecasting-Machine-Learning-Project/
│
├── app.py
├── analysis.ipynb
├── requirements.txt
├── label_encoders.pkl
├── xgboost_demand_model.pkl
├── .gitignore
└── README.md
```

## How to Run the App

First, install the required packages:

```bash
pip install -r requirements.txt
```

Then run the Streamlit app:

```bash
streamlit run app.py
```

## Input Features

| Feature | Description |
|---|---|
| Price | Product price |
| Discount | Discount percentage |
| Inventory Level | Available stock level |
| Promotion | Whether the product is under promotion |
| Competitor Pricing | Price of similar competitor products |
| Category | Product category |

## Product Categories

The app uses the following product categories:

| Number | Category |
|---|---|
| 0 | Clothing |
| 1 | Electronics |
| 2 | Furniture |
| 3 | Groceries |
| 4 | Toys |

In the Streamlit app, users see the category names instead of numbers.

## Model

The model used in this project is an XGBoost regression model. The trained model is saved as:

```text
xgboost_demand_model.pkl
```

The label encoders are saved as:

```text
label_encoders.pkl
```

## Purpose of the Project

This project was created to practice machine learning model development, regression, model saving, and building a simple web app using Streamlit.

## Future Improvements

- Add model performance metrics to the README
- Improve the app design
- Deploy the app online using Streamlit Community Cloud
- Add visual charts for demand trends
- Add more features for better prediction accuracy
