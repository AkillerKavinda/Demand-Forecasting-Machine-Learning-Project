import streamlit as st
import pandas as pd
import pickle 

@st.cache_resource
def load_artifacts():
    with open("xgboost_demand_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("label_encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    
    return model, encoders

model, label_encoders = load_artifacts()

st.title("Demand Forecasting App")

st.divider()

st.header("Input Features")

price = st.number_input("Price", min_value=0.0, value=50.0)
discount = st.number_input("Discount (%)", min_value=0, max_value=100, value=10)
inventory_level = st.number_input("Inventory Level", min_value=0, value=100)
promotion = st.selectbox("Promotion", [0, 1])
competitor_pricing = st.number_input("Competitor Price", min_value=0.0, value=50.0)

category_map = {
    0: "Clothing",
    1: "Electronics",
    2: "Furniture",
    3: "Groceries",
    4: "Toys"
}

category_name = st.selectbox(
    "Category",
    list(category_map.values())
)

category_number = [key for key, value in category_map.items() if value == category_name][0]

input_data = pd.DataFrame({
    "Price": [price],
    "Discount": [discount], 
    "Inventory Level": [inventory_level],
    "Promotion": [promotion],
    "Competitor Pricing": [competitor_pricing],
    "Category": [category_number]
})

for col, encoder in label_encoders.items():
    if col in input_data.columns and col != "Category":
        input_data[col] = encoder.transform(input_data[col])

st.divider()

if st.button("Predict Demand"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Demand: {int(prediction)}")