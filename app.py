import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("house_price_model.pkl")

st.set_page_config(
    page_title="House Price Prediction", page_icon="🏠", layout="centered"
)

st.title("House Price Prediction")
st.write(
    "Enter information about a neighborhood or Local area"
    "to estimate its typical house price."
)

longitude = st.number_input("Longitude", value=-122.23, format="%.5f")

latitude = st.number_input("Latitude", value=37.88, format="%.5f")

housing_median_age = st.number_input(
    "Average Age of Homes in the Area", min_value=1.0, value=41.0
)

total_rooms = st.number_input("Total Rooms in the Area", min_value=1.0, value=2000.0)

total_bedrooms = st.number_input(
    "Total Bedrooms in the Area", min_value=1.0, value=400.0
)

population = st.number_input("Population in the Area", min_value=1.0, value=1000.0)

households = st.number_input("Households in the Area", min_value=1.0, value=400.0)

median_income = st.number_input(
    "Average Household Income in the Area", min_value=0.0, value=5.0
)

ocean_proximity = st.selectbox(
    "Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
)
st.subheader("Selected Area on Map")

map_data = pd.DataFrame({
    "latitude": [latitude],
    "longitude": [longitude]
})

st.map(map_data, zoom=8)
if st.button("Predict Price"):
    new_house = pd.DataFrame(
        {
            "longitude": [longitude],
            "latitude": [latitude],
            "housing_median_age": [housing_median_age],
            "total_rooms": [total_rooms],
            "total_bedrooms": [total_bedrooms],
            "population": [population],
            "households": [households],
            "median_income": [median_income],
            "ocean_proximity": [ocean_proximity],
        }
    )

    prediction = model.predict(new_house)[0]

    st.success(f"Estimated Typical House Price in this Area: ${prediction:,.2f}")
