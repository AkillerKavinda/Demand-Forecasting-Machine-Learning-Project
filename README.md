# Demand Forecasting Machine Learning Project

This project predicts product demand using a machine learning regression model.

I built a Streamlit web app where users can enter product details such as price, discount, inventory level, promotion status, competitor pricing, and product category. The app then predicts the expected product demand.

## App Interface

![Demand Forecasting App Interface](Images/interface.png)

## Project Overview

Demand forecasting helps businesses estimate how much of a product customers may buy. This can support stock planning, pricing decisions, and inventory management.

In this project, I trained an XGBoost regression model to predict demand based on product and market-related features.

## What I Did

- Explored and prepared the demand forecasting dataset
- Encoded categorical data for machine learning
- Trained an XGBoost regression model
- Saved the trained model using Pickle
- Saved the label encoders for use in the app
- Built a Streamlit web app for predictions
- Added readable product category names in the app instead of showing category numbers
- Organized the project and uploaded it to GitHub

## Features Used for Prediction

| Feature | Description |
|---|---|
| Price | Product price |
| Discount | Discount percentage |
| Inventory Level | Available stock level |
| Promotion | Whether the product is under promotion |
| Competitor Pricing | Competitor product price |
| Category | Product category |

## Product Categories

| Number | Category |
|---|---|
| 0 | Clothing |
| 1 | Electronics |
| 2 | Furniture |
| 3 | Groceries |
| 4 | Toys |

The model uses numbers internally, but the app shows clear category names to users.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Pickle

## Project Purpose

The purpose of this project was to practice building a complete machine learning regression project and turning it into a simple web app.

Through this project, I practiced data preprocessing, model training, model saving, and Streamlit app development.

## Future Improvements

- Add model performance metrics
- Improve the app design
- Add charts for demand insights
- Deploy the app online
