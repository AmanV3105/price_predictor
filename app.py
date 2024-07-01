import streamlit as st
import pickle
import json

# Load the pre-trained models
# with open('car_price_predictor.pkl', 'rb') as file:
#     car_model = pickle.load(file)

with open('property_price_predictor_banglore.pkl', 'rb') as file:
    property_model = pickle.load(file)

# Load the columns for property prediction
with open('columns.json', 'r') as file:
    data_columns = json.load(file)['data_columns']

# def car_price_prediction(inputs):
#     # Assume `inputs` is a list or array of the features needed for prediction
#     return car_model.predict([inputs])[0]

def property_price_prediction(inputs):
    # Assume `inputs` is a list or array of the features needed for prediction
    return property_model.predict([inputs])[0]

# Streamlit App Layout
st.title('Price Predictor App')

st.sidebar.title('Select Predictor')
predictor = st.sidebar.selectbox('Predictor', ['Car Price', 'Property Price'])

# if predictor == 'Car Price':
#     st.header('Car Price Predictor')
#     # Example input fields for car price prediction
#     car_year = st.number_input('Year', 2000, 2024)
#     car_mileage = st.number_input('Mileage', 0)
#     car_hp = st.number_input('Horsepower', 0)
    
#     # Add more fields as needed for your model

#     if st.button('Predict Car Price'):
#         car_inputs = [car_year, car_mileage, car_hp]  # Add other features here
#         car_price = car_price_prediction(car_inputs)
#         st.write(f'The predicted car price is ${car_price:,.2f}')
        
if predictor == 'Property Price':
    st.header('Property Price Predictor')
    
    # Input fields for property price prediction
    total_sqft = st.number_input('Total Square Feet', 0)
    bath = st.number_input('Bathrooms', 1)
    bhk = st.number_input('BHK', 1)
    
    # Dropdown for location selection
    location = st.selectbox('Location', data_columns[3:])  # Locations are in columns.json from index 3 onwards
    
    if st.button('Predict Property Price'):
        # Prepare the input array for the model
        location_index = data_columns.index(location)
        property_inputs = [0] * len(data_columns)
        property_inputs[0] = total_sqft
        property_inputs[1] = bath
        property_inputs[2] = bhk
        property_inputs[location_index] = 1
        
        property_price = property_price_prediction(property_inputs)
        st.write(f'The predicted property price is ₹{property_price:,.2f} lakh')
