# House Price Prediction

A machine-learning web application that predicts house prices using property and location details.

## Live Demo

[Open the House Price Prediction App](https://house-price-prediction-kk6w8fda62aghzgxbb8t.streamlit.app)

## Features

- Predicts estimated house prices
- Uses a Random Forest regression model
- Handles missing values automatically
- Processes categorical location data
- Provides an interactive Streamlit interface

## Dataset

The model uses a California housing dataset with the following features:

- Longitude
- Latitude
- Housing median age
- Total rooms
- Total bedrooms
- Population
- Households
- Median income
- Ocean proximity

The prediction target is `median_house_value`.

## Model Performance

The model achieved:

- Mean Absolute Error: approximately `$31,636`
- Root Mean Squared Error: approximately `$48,978`
- R² Score: approximately `0.817`

The R² score means the model explains about 81.7% of the variation in house prices in the test data.

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- Random Forest
- joblib
- Streamlit

## Run Locally

Clone the repository:

```bash
git clone https://github.com/hiten95/house-price-prediction.git
cd house-price-prediction